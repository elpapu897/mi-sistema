"""Isolated watchdog fixtures: never contact Telegram or trigger live jobs."""
import importlib
import unittest
from datetime import datetime, timezone

class WatchdogTests(unittest.TestCase):
    def test_no_activation_has_no_effects(self):
        try:
            w = importlib.import_module('watchdog')
        except ModuleNotFoundError:
            self.fail('watchdog decision engine is not implemented')
        original = {'keep': 'untouched'}
        actions, state = w.decide({'activated_at': None}, [], [], original,
                                  datetime.now(timezone.utc), {}, False)
        self.assertEqual(actions, [])
        self.assertEqual(state, original)

    def test_failure_one_retry_then_second_failure_one_alert(self):
        import watchdog as w
        now = datetime.fromisoformat('2026-09-19T12:05:00+00:00')
        manifest = {'activated_at': '2026-09-19T11:59:00+00:00', 'timezone': 'UTC',
                    'jobs': [{'id': 'j1', 'role': 'OPS', 'schedule': '0 * * * *'}]}
        jobs = [{'id': 'j1', 'enabled': True, 'next_run_at': '2026-09-19T13:00:00+00:00'}]
        rows = [{'id': 'e1', 'job_id': 'j1', 'status': 'failed',
                 'claimed_at': '2026-09-19T12:00:02+00:00',
                 'finished_at': '2026-09-19T12:04:00+00:00'}]
        actions, state = w.decide(manifest, jobs, rows, {}, now, {}, True)
        self.assertEqual([a['kind'] for a in actions], ['retry'])
        self.assertEqual(w.decide(manifest, jobs, rows, state, now, {}, True)[0], [])
        rows.append(dict(rows[0], id='e2', claimed_at='2026-09-19T12:06:00+00:00',
                         finished_at='2026-09-19T12:09:00+00:00'))
        now = datetime.fromisoformat('2026-09-19T12:10:00+00:00')
        actions, state = w.decide(manifest, jobs, rows, state, now, {}, True)
        self.assertEqual([a['kind'] for a in actions], ['alert'])
        self.assertEqual(w.decide(manifest, jobs, rows, state, now, {}, True)[0], [])

class MonitorTests(unittest.TestCase):
    def setUp(self):
        import watchdog
        self.w = watchdog
        self.now = datetime.fromisoformat('2026-09-19T12:20:00+00:00')
        self.manifest = {'activated_at': '2026-09-19T11:59:00+00:00', 'timezone': 'UTC',
                         'jobs': [{'id': 'j1', 'role': 'OPS', 'schedule': '0 * * * *'}]}
        self.jobs = [{'id': 'j1', 'enabled': True, 'next_run_at': '2026-09-19T13:00:00+00:00'}]
        self.e = {'id': 'e1', 'job_id': 'j1', 'status': 'completed',
                  'claimed_at': '2026-09-19T12:00:02+00:00',
                  'finished_at': '2026-09-19T12:04:00+00:00'}
        self.art = {('OPS', '2026-09-19'): {'size': 25, 'mtime': self.now.timestamp()}}

    def decision(self, rows=None, state=None, art=None, active=True):
        return self.w.decide(self.manifest, self.jobs, rows or [], state or {}, self.now,
                             self.art if art is None else art, active)

    def test_missed_run_after_grace_dedup(self):
        actions, state = self.decision()
        self.assertEqual([a['code'] for a in actions], ['missed'])
        self.assertEqual(self.decision(state=state)[0], [])

    def test_healthy_silent(self):
        self.assertEqual(self.decision([self.e])[0], [])

    def test_paused_ignore(self):
        for fields in ({'enabled': False}, {'state': 'paused'}, {'paused_at': 'now'}):
            with self.subTest(fields=fields):
                self.jobs[0].update(fields)
                self.assertEqual(self.decision()[0], [])

    def test_artifact_missing_empty_and_stale(self):
        for art in ({}, {('OPS', '2026-09-19'): {'size': 0, 'mtime': self.now.timestamp()}},
                    {('OPS', '2026-09-19'): {'size': 12, 'mtime': 1}}):
            with self.subTest(art=art):
                actions, _ = self.decision([self.e], art=art)
                self.assertEqual([a['code'] for a in actions], ['artifact_missing'])

    def test_gateway_down_alert_once_per_outage(self):
        actions, state = self.decision([self.e], active=False)
        self.assertEqual([a['code'] for a in actions], ['gateway_down'])
        self.assertEqual(self.decision([self.e], state, active=False)[0], [])
        _, state = self.decision([self.e], state, active=True)
        self.assertEqual(len(self.decision([self.e], state, active=False)[0]), 1)

    def test_hung_alert_only_gateway_owner_never_killed(self):
        self.now = datetime.fromisoformat('2026-09-19T12:30:00+00:00')
        row = dict(self.e, status='running', pid=123, process_started_at=456)
        actions, _ = self.decision([row])
        self.assertEqual([a['code'] for a in actions], ['hung_unproven_owner'])
        self.assertTrue(all(a['kind'] != 'kill' for a in actions))

    def test_jefe_delivery_only_failure_never_rerun(self):
        self.manifest['jobs'][0]['role'] = 'JEFE'
        self.jobs[0].update(last_delivery_error='delivery failed', last_status='ok',
                            last_run_at=self.e['finished_at'])
        actions, _ = self.decision([self.e], art={('JEFE', '2026-09-19'): {'size': 30, 'mtime': self.now.timestamp()}})
        self.assertEqual([a['code'] for a in actions], ['delivery_failed'])
        self.assertTrue(all(a['kind'] != 'retry' for a in actions))

    def test_existing_native_retry_running_suppresses_retry(self):
        actions, _ = self.decision([dict(self.e, status='failed'),
                                   dict(self.e, id='e2', status='running', claimed_at='2026-09-19T12:10:00+00:00')])
        self.assertEqual(actions, [])

    def test_frequent_guard_older_missed_slot_detected(self):
        self.manifest['jobs'][0]['schedule'] = '*/5 * * * *'
        actions, _ = self.decision()
        self.assertIn('missed', [a['code'] for a in actions])

    def test_old_state_pruned(self):
        _, state = self.decision([self.e], {'cycles': {'old': {'slot': '2020-01-01T00:00:00+00:00'}}})
        self.assertNotIn('old', state['cycles'])

if __name__ == '__main__':
    unittest.main()
