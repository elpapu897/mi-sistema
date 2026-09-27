#!/usr/bin/env python3
"""External, approval-gated GONVRA watchdog. Native Hermes owns execution.

No agent/provider calls. Never kills: the inspected native scheduler runs cron
in gateway threads, not provably distinct worker processes. PID identity alone
is insufficient permission to kill a process. All hangs are alert-only.
"""
from __future__ import annotations
import copy
import sys
sys.dont_write_bytecode = True
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from croniter import croniter

RETENTION = timedelta(days=14)
GRACE = timedelta(minutes=15)
HUNG = timedelta(minutes=25)
ACTIVE = {'claimed', 'running'}

def stamp(value):
    result = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Timezone-aware timestamps required')
    return result

def slot_at(expr, now):
    return croniter(expr, now + timedelta(microseconds=1)).get_prev(datetime)

def runnable(job):
    return bool(job and job.get('enabled', True) and job.get('state') != 'paused'
                and not job.get('paused_at'))

def artifact_ok(artifacts, role, execution, tz):
    started = stamp(execution.get('started_at') or execution['claimed_at'])
    art = artifacts.get((role, started.astimezone(tz).date().isoformat()), {})
    return art.get('size', 0) > 0 and art.get('mtime', 0) >= started.timestamp() - 2

def exact_owner_matches(execution, observed):
    """Necessary, NOT sufficient, condition for ownership. No signal is sent."""
    return bool(execution.get('pid') and execution.get('process_started_at') is not None
                and observed.get('pid') == execution['pid']
                and observed.get('starttime') == execution['process_started_at'])

def decide(manifest, jobs, executions, state, now, artifacts, gateway_active):
    """Pure decision function. Returned reservations must persist BEFORE effects.

    Fixture inputs only; does not read files, inspect processes or send messages.
    Cached ledger rows survive native terminal pruning (native limit: 1000).
    """
    state = copy.deepcopy(state)
    if not manifest.get('activated_at') or stamp(manifest['activated_at']) > now:
        return [], state
    tz = ZoneInfo(manifest.get('timezone', 'America/Argentina/Buenos_Aires'))
    now = now.astimezone(tz)
    activation = stamp(manifest['activated_at'])
    cutoff = max(activation, now - RETENTION)
    actions = []
    cycles = {k: v for k, v in state.get('cycles', {}).items() if stamp(v['slot']) >= cutoff}
    state['cycles'] = cycles
    history = state.setdefault('job_observations', {})
    ids = {s['id'] for s in manifest['jobs']}
    history = {k: v for k, v in history.items() if k in ids}
    state['job_observations'] = history
    cached = state.get('executions', {})
    for e in executions:
        if e['job_id'] in ids:
            # Never retain provider messages, prompts or credentials in state.
            cached[e['id']] = {k: v for k, v in e.items() if k in {
                'id', 'job_id', 'status', 'source', 'claimed_at', 'started_at',
                'finished_at', 'pid', 'process_started_at'}}
    cached = {k: v for k, v in cached.items() if stamp(v['claimed_at']) >= cutoff}
    state['executions'] = cached
    if gateway_active:
        state.pop('gateway_down', None)
    elif not state.get('gateway_down'):
        actions.append({'kind': 'alert', 'code': 'gateway_down'})
        state['gateway_down'] = now.isoformat()
    live = {j['id']: j for j in jobs}

    def alert(cycle, code, spec, key, **extra):
        if code not in cycle['alerts']:
            cycle['alerts'].append(code)
            actions.append({'kind': 'alert', 'code': code, 'job_id': spec['id'],
                            'role': spec['role'], 'cycle': key, **extra})

    for spec in manifest['jobs']:
        job = live.get(spec['id'])
        previous = history.get(spec['id'], {})
        if job is None or not runnable(job):
            history[spec['id']] = {'paused': True, 'since': now.isoformat()}
            continue
        start = max(cutoff, stamp(previous.get('since', cutoff.isoformat())))
        if previous.get('paused'):
            start = now
        history[spec['id']] = {'since': start.isoformat(), 'paused': False}
        expr = spec['schedule']
        latest_slot = slot_at(expr, now)
        iterator = croniter(expr, start.astimezone(tz) - timedelta(microseconds=1))
        by_slot = {}
        rows = sorted((e for e in cached.values() if e['job_id'] == spec['id']),
                      key=lambda e: (e['claimed_at'], e['id']))
        for e in rows:
            eslot = slot_at(expr, stamp(e['claimed_at']).astimezone(tz))
            by_slot.setdefault(eslot.isoformat(), []).append(e)
        inflight = any(e['status'] in ACTIVE for e in rows)
        for _ in range(25000):  # >= 14 days of a once-per-minute schedule
            slot = iterator.get_next(datetime)
            if slot > now:
                break
            key = spec['id'] + '|' + slot.isoformat()
            cycle = cycles.setdefault(key, {'slot': slot.isoformat(), 'alerts': []})
            attempts = by_slot.get(slot.isoformat(), [])
            active = [e for e in attempts if e['status'] in ACTIVE]
            if active:
                for e in active:
                    if now - stamp(e.get('started_at') or e['claimed_at']) >= HUNG:
                        alert(cycle, 'hung_unproven_owner', spec, key, execution_id=e['id'])
                continue
            successes = [e for e in attempts if e['status'] == 'completed']
            if successes:
                e = successes[-1]
                if not artifact_ok(artifacts, spec['role'], e, tz):
                    alert(cycle, 'artifact_missing', spec, key)
                # The ledger says completed even when delivery failed. Never run
                # the JEFE producer again merely to redeliver a Telegram report.
                last_run = job.get('last_run_at')
                if job.get('last_delivery_error') and last_run and (
                    stamp(last_run) >= stamp(e['claimed_at']) and
                    (not e.get('finished_at') or abs((stamp(last_run) - stamp(e['finished_at'])).total_seconds()) < 60)
                ):
                    alert(cycle, 'delivery_failed', spec, key)
                continue
            if any(e['status'] == 'unknown' for e in attempts):
                alert(cycle, 'unknown_side_effects', spec, key)
                continue
            failed = [e for e in attempts if e['status'] == 'failed']
            if len(failed) >= 2:
                alert(cycle, 'failed_twice', spec, key)
            elif failed:
                retry = cycle.get('retry')
                if retry:
                    if now - stamp(retry['reserved_at']) >= GRACE:
                        alert(cycle, 'retry_not_observed', spec, key)
                    continue
                if inflight or job.get('fire_claim') or job.get('run_claim'):
                    continue
                if slot != latest_slot:
                    alert(cycle, 'failed_cycle_elapsed', spec, key)
                    continue
                nxt = job.get('next_run_at')
                # A due/near-due native run wins; never overwrite a queued retry
                # or race the upcoming scheduled slot for frequent guard jobs.
                if nxt and stamp(nxt) <= now + timedelta(seconds=65):
                    continue
                if not gateway_active:
                    continue
                cycle['retry'] = {'reserved_at': now.isoformat(), 'after': failed[-1]['id']}
                actions.append({'kind': 'retry', 'job_id': spec['id'], 'role': spec['role'],
                                'cycle': key, 'after': failed[-1]['id']})
            elif not attempts and now - slot >= GRACE:
                alert(cycle, 'missed', spec, key)
        else:
            raise ValueError('Schedule exceeds bounded 14-day scan')
    return actions, state
