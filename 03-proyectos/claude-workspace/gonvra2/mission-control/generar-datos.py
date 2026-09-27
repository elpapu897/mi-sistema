#!/usr/bin/env python3
"""Genera datos.json para el Mission Control de GONVRA con el estado real del equipo."""
import json, os, re, subprocess, datetime
from pathlib import Path

BASE = Path.home() / "Claude" / "gonvra2"
OUT  = BASE / "mission-control" / "datos.json"

# slug: emoji, nombre, rol, grupo, personalidad, modelo, horas(cron), herramientas
AG = {
 "jefe":("🧠","JEFE","Coordina y manda el resumen diario","nucleo",
   "Directo y breve. Prioriza por pesos, no por prolijidad. Odia el relleno.",
   "astra",[21],["Lectura de informes","Telegram","Kanban"]),
 "analista":("📊","ANALISTA","Números, embudo y carritos","nucleo",
   "Frío con los datos. Si no hay dato, dice 'no sé'. Nunca estima sin avisar.",
   "sol",[6],["Shopify API","Meta Events","Analytics"]),
 "guardia":("🚨","GUARDIA","Vigila la tienda y avisa cada venta","nucleo",
   "Callado. Solo habla si hay un problema o entró una venta.",
   "sol",[0,4,8,12,16,20,22],["HTTP/curl","Shopify API","Telegram"]),
 "cro":("🔬","CRO","Sube la conversión: un test por vez","plata",
   "Obsesivo con el celular. Cuantifica todo en pesos. Un test por vez, sin dispersarse.",
   "astra",[13],["Navegador","Shopify","Capturas"]),
 "cazador":("🎣","CAZADOR","Recupera carritos abandonados","plata",
   "Persuasivo pero no pesado. Escribe como una persona, no como un robot.",
   "sol",[19],["Shopify (carritos)","Redacción"]),
 "precios":("🏷️","PRECIOS","Margen real y CPA máximo","plata",
   "Desconfiado. Marca cada supuesto como supuesto. No autoriza gastar sin números.",
   "sol",[],["Shopify (costos)","Cálculo de márgenes"]),
 "copy":("✍️","COPY","Textos de la web y objeciones","contenido",
   "Argentino, claro y honesto. Cero urgencia falsa. Escribe como habla la gente.",
   "astra",[9],["Web","Shopify","Análisis de copy"]),
 "creativo":("🎨","CREATIVO","Imágenes, placas y videos","contenido",
   "Visual. Nunca entrega una sola opción: siempre variantes para elegir.",
   "sol",[15],["Replicate","ffmpeg","genimage.py"]),
 "tiktoker":("📱","TIKTOKER","Guiones de video para TikTok","contenido",
   "Piensa en los primeros 2 segundos. Guiones grabables con celular, sin producción.",
   "sol",[10],["video-intel.py","TikTok research"]),
 "instagramer":("📸","INSTAGRAMER","Reels, carruseles e historias","contenido",
   "Cuida el feed como marca. Prioriza lo que la gente guarda, no lo que le gusta.",
   "sol",[11],["video-intel.py","Instagram research"]),
 "espia":("🕵️","ESPIA","Competencia y anuncios que funcionan","contenido",
   "Paciente. Busca anuncios con 30+ días activos: esos son los que dan plata.",
   "sol",[2],["Biblioteca de anuncios Meta","Web","video-intel.py"]),
 "mediabuyer":("🎯","MEDIABUYER","Campañas de Meta","pauta",
   "Disciplinado con el presupuesto. Arma campañas SIEMPRE en pausa. Nunca gasta solo.",
   "sol",[],["Meta Ads API"]),
 "tienda":("🛠️","TIENDA","Cambios en el tema de Shopify","operacion",
   "Prudente. Nunca toca el tema publicado: siempre sobre una copia.",
   "sol",[],["Shopify CLI","Theme push/pull"]),
 "mensajero":("📬","MENSAJERO","Gmail y WhatsApp","operacion",
   "Rápido con quien está por comprar. Redacta, nunca envía sin permiso.",
   "sol",[],["Gmail API","WhatsApp"]),
 "legal":("⚖️","LEGAL","Cumplimiento argentino","operacion",
   "Estricto. Prefiere sacar una promesa antes que arriesgar una multa.",
   "sol",[],["Web","Lectura de políticas"]),
}
GRUPOS = {"nucleo":"Núcleo · coordinan y vigilan","plata":"Plata directa · convierten lo que ya entra",
          "contenido":"Contenido · traen gente","pauta":"Pauta","operacion":"Operación"}
MODELOS = {"astra":{"nombre":"GPT-6 Astra","prov":"OpenAI Codex","tipo":"potente"},
           "sol":{"nombre":"GPT-5.6 Sol","prov":"OpenAI Codex","tipo":"económico"}}
HERRAM = [
 {"n":"Shopify CLI","est":"ok","d":"Edita el tema (theme pull/push)"},
 {"n":"Meta Ads","est":"parcial","d":"Píxel conectado · pauta en pausa"},
 {"n":"WhatsApp","est":"falta","d":"Sin conectar todavía"},
 {"n":"TikTok API","est":"falta","d":"Falta aprobación de TikTok"},
]

def resumen(t, n=400):
    t = re.sub(r"^---.*?---", "", t, flags=re.S)
    t = re.sub(r"[#*`>|]", "", t)
    ls = [l.strip() for l in t.split("\n") if len(l.strip()) > 40]
    return (" ".join(ls)[:n] + "…") if ls else t[:n].strip()


def frases(txt, n=3):
    """Saca frases con contenido real de un informe."""
    txt = re.sub(r"^---.*?---", "", txt, flags=re.S)
    txt = re.sub(r"[#*`>|\[\]]", "", txt)
    out=[]
    for l in re.split(r"[\n.]", txt):
        l=l.strip()
        if 45 < len(l) < 190 and not l.lower().startswith(("fecha","estado","http","- [")):
            out.append(l if l.endswith(".") else l+".")
        if len(out)>=n: break
    return out

NOMBRES = {"jefe":"JEFE","analista":"ANALISTA","guardia":"GUARDIA","cro":"CRO","cazador":"CAZADOR",
 "precios":"PRECIOS","copy":"COPY","creativo":"CREATIVO","tiktoker":"TIKTOKER",
 "instagramer":"INSTAGRAMER","espia":"ESPIA","mediabuyer":"MEDIABUYER","tienda":"TIENDA",
 "mensajero":"MENSAJERO","legal":"LEGAL"}

def conversacion(agentes):
    """Chat del equipo. Usa conversaciones/chat.md si existe; si no, frases reales de los informes."""
    compartido = BASE / "conversaciones" / "chat.md"
    if compartido.exists():
        msgs = []
        pat = re.compile(r"^\s*[-*]?\s*\[?([0-9]{1,2}:[0-9]{2})?\]?\s*([A-ZÁÉÍÓÚÑ]{3,14})\s*(?:->|→)?\s*([A-ZÁÉÍÓÚÑ]{3,14})?\s*:\s*(.+)$")
        for ln in compartido.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = pat.match(ln)
            if not m: continue
            hora, de, para, txt = m.groups()
            slug = next((k for k, v in NOMBRES.items() if v == de), None)
            if slug and len(txt.strip()) > 8:
                a = next((x for x in agentes if x["slug"] == slug), None)
                msgs.append({"agente": de, "emoji": a["emoji"] if a else "\U0001F916", "slug": slug,
                             "para": para if para in NOMBRES.values() else None,
                             "hora": hora or "", "iso": "", "texto": txt.strip()[:200]})
        if msgs: return msgs[-40:]
    msgs = []
    for a in agentes:
        if not a.get("_txt"): continue
        for f in frases(a["_txt"], 2):
            para = None
            for slug2, nm2 in NOMBRES.items():
                if slug2 != a["slug"] and re.search(r"\b" + nm2 + r"\b", f):
                    para = nm2; break
            msgs.append({"agente": a["nombre"], "emoji": a["emoji"], "slug": a["slug"], "para": para,
                         "hora": a["ultima_fecha"] or "", "iso": a.get("ultima_iso") or "", "texto": f})
    msgs.sort(key=lambda m: m["iso"])
    return msgs[-40:]

def kanban():
    out = {"done":0,"running":0,"blocked":0,"ready":0,"tareas":[]}
    try:
        s = subprocess.run(["hermes","kanban","stats"],capture_output=True,text=True,timeout=25).stdout
        for k in ["done","running","blocked","ready"]:
            if (m := re.search(rf"{k}\s+(\d+)", s)): out[k] = int(m.group(1))
        l = subprocess.run(["hermes","kanban","list"],capture_output=True,text=True,timeout=25).stdout
        for ln in l.splitlines():
            if (m := re.match(r"\s*[✓⊘●]?\s*(t_\w+)\s+(\w+)\s+(\S+)\s+(.+)", ln.strip())):
                out["tareas"].append({"id":m.group(1),"estado":m.group(2),
                                      "agente":m.group(3).replace("gonvra-",""),"titulo":m.group(4).strip()[:70]})
    except Exception: pass
    return out

def automatizaciones_vivas():
    """Estado real de n8n y del tunel. Nada escrito a mano."""
    import os, sqlite3, json as _j, urllib.request
    out = []

    # workflows activos de n8n
    try:
        c = sqlite3.connect("file:" + os.path.expanduser("~/.n8n/database.sqlite")
                            + "?mode=ro", uri=True)
        n = len([r for r in c.execute(
            "select 1 from workflow_entity where active=1 and activeVersionId is not null")])
        c.close()
        out.append({"n": "n8n", "est": "ok" if n else "falta",
                    "d": f"{n} automatizaciones corriendo"})
    except Exception:
        out.append({"n": "n8n", "est": "falta", "d": "No se pudo leer"})

    # tunel publico
    try:
        url = open(os.path.expanduser("~/.hermes/gonvra-url-publica.txt")).read().strip()
        req = urllib.request.Request(url + "/webhook/gonvra-venta", data=b"{}",
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as r:
            vivo = r.status == 200
        out.append({"n": "Tunel publico", "est": "ok" if vivo else "parcial",
                    "d": "Recibe ventas y comentarios al instante"})
    except Exception:
        out.append({"n": "Tunel publico", "est": "falta",
                    "d": "No responde - los webhooks no llegan"})

    return out

def herramientas_locales():
    """Chequea de verdad las herramientas de la maquina.
    Nada de listas escritas a mano: si no responde, no esta 'ok'."""
    import os, shutil, json as _j, urllib.request
    out = []

    # ffmpeg
    out.append({"n": "ffmpeg", "est": "ok" if shutil.which("ffmpeg") else "falta",
                "d": "Arma y edita videos" if shutil.which("ffmpeg") else "No esta instalado"})

    # scripts propios
    for ruta, nombre, desc in (
        ("~/Claude/scripts/video-intel.py", "video-intel.py", "Espia videos sin gastar tokens"),
        ("~/Claude/scripts/genimage-replicate.py", "genimage-replicate.py", "Genera imagenes"),
    ):
        hay = os.path.exists(os.path.expanduser(ruta))
        out.append({"n": nombre, "est": "ok" if hay else "falta",
                    "d": desc if hay else "Falta el script"})

    # Replicate: probar la cuenta de verdad.
    # El archivo de secretos MANDA sobre la variable de entorno: la del entorno
    # puede ser una clave vieja que quedo dando vueltas.
    tok = None
    try:
        for l in open(os.path.expanduser("~/.hermes/.gonvra-secrets.env"),
                      encoding="utf-8"):
            if l.startswith("REPLICATE_API_TOKEN="):
                tok = l.split("=", 1)[1].strip()
                break
    except Exception:
        pass
    if not tok:
        tok = os.environ.get("REPLICATE_API_TOKEN")
    if not tok:
        out.append({"n": "Replicate", "est": "falta", "d": "Sin clave"})
    else:
        try:
            # Replicate devuelve 403 con el User-Agent por defecto de Python
            r = urllib.request.Request(
                "https://api.replicate.com/v1/account",
                headers={"Authorization": "Bearer " + tok,
                         "User-Agent": "gonvra/1.0"})
            with urllib.request.urlopen(r, timeout=12) as resp:
                d = _j.loads(resp.read().decode())
            # mostrar tambien cuanto se gasto hoy en video
            gasto = 0.0
            try:
                import datetime as _dt
                g = _j.load(open(os.path.expanduser(
                    "~/.hermes/gonvra-gasto-replicate.json")))
                gasto = float(g.get(_dt.date.today().isoformat(), 0))
            except Exception:
                pass
            detalle = "Imagenes US$0.003 · video US$0.28"
            if gasto:
                detalle += f" · hoy US${gasto:.2f} de US$3"
            out.append({"n": "Replicate", "est": "ok", "d": detalle})
        except Exception as e:
            cod = getattr(e, "code", "?")
            out.append({"n": "Replicate", "est": "falta",
                        "d": f"La clave no sirve (HTTP {cod}) - hay que renovarla"})

    # Telegram = el motor de agentes vivo
    pid_ok = False
    try:
        pid = _j.load(open(os.path.expanduser("~/.hermes/gateway.pid")))["pid"]
        os.kill(pid, 0); pid_ok = True
    except Exception:
        pass
    out.append({"n": "Telegram", "est": "ok" if pid_ok else "falta",
                "d": "Avisos y aprobaciones" if pid_ok else "El motor esta caido"})
    return out

def shopify_vivo():
    """Lee pedidos, carritos y clientes DE VERDAD desde Shopify.
    El token sale del archivo cerrado, nunca se escribe aca."""
    import os, json as _j, urllib.request
    tok = None
    try:
        for l in open(os.path.expanduser("~/.hermes/.gonvra-secrets.env"), encoding="utf-8"):
            if l.startswith("SHOPIFY_ACCESS_TOKEN="):
                tok = l.split("=", 1)[1].strip(); break
    except Exception:
        pass
    if not tok:
        return None
    base = "https://jm60sa-cp.myshopify.com/admin/api/2026-01"
    def pedir(ruta):
        r = urllib.request.Request(base + ruta, headers={"X-Shopify-Access-Token": tok})
        with urllib.request.urlopen(r, timeout=20) as resp:
            return _j.loads(resp.read().decode())
    try:
        ords = pedir("/orders.json?status=any&limit=50").get("orders", [])
        chks = pedir("/checkouts.json?limit=50").get("checkouts", [])
    except Exception:
        return None
    facturado = sum(float(o.get("total_price") or 0) for o in ords)
    hoy = datetime.date.today().isoformat()
    return {
        "pedidos": len(ords),
        "pedidos_hoy": sum(1 for o in ords if (o.get("created_at") or "")[:10] == hoy),
        "facturado": round(facturado, 2),
        "carritos_abandonados": len(chks),
        "plata_en_carritos": round(sum(float(c.get("total_price") or 0) for c in chks), 2),
        "ultimo_pedido": (ords[0].get("created_at", "")[:16] if ords else None),
    }

def instagram_real():
    """Chequea Instagram DE VERDAD contra la API. El token se lee del archivo
    cerrado ~/.hermes/.gonvra-secrets.env, nunca se escribe aca."""
    import os, json as _j, urllib.request
    tok = None
    try:
        for linea in open(os.path.expanduser("~/.hermes/.gonvra-secrets.env"), encoding="utf-8"):
            if linea.startswith("INSTAGRAM_ACCESS_TOKEN="):
                tok = linea.split("=", 1)[1].strip()
                break
    except Exception:
        pass
    if not tok:
        return {"n": "Instagram API", "est": "falta", "d": "Sin token"}
    try:
        u = ("https://graph.instagram.com/me?fields=username,account_type"
             "&access_token=" + tok)
        with urllib.request.urlopen(u, timeout=15) as r:
            d = _j.loads(r.read().decode())
        return {"n": "Instagram API", "est": "ok",
                "d": "@%s (%s) - puede publicar" % (d.get("username","?"),
                                                    d.get("account_type","?"))}
    except Exception:
        return {"n": "Instagram API", "est": "falta", "d": "El token dejo de andar"}

def mcps_reales():
    """Lee los MCP realmente conectados en Hermes (config.yaml).
    Nada de listas escritas a mano: si no esta en config, no existe."""
    try:
        import yaml as _y
        cfg = _y.safe_load(open("/home/matiigonzz/.hermes/config.yaml", encoding="utf-8")) or {}
    except Exception:
        return []
    srv = cfg.get("mcp_servers") or {}
    # Conectado != funcionando. Lo que se probo y NO trae datos se marca parcial.
    PROBLEMAS = {
        "fbads": ("parcial", "Conecta, pero Facebook lo bloquea (403 anti-bot)"),
        # gmail: verificado de verdad, no a mano -> existe la credencial OAuth?
        "gmail": (("ok", "15 herramientas · autorizado con gonvra0@gmail.com")
                  if __import__("os").path.exists(__import__("os").path.expanduser(
                      "~/.google_workspace_mcp/credentials/gonvra0@gmail.com.json"))
                  else ("parcial", "15 herramientas · falta autorizar en Google")),
        "shopify": ("ok", "14 herramientas · lee pedidos, clientes y carritos"),
    }
    out = []
    for nombre, datos in srv.items():
        activo = (datos or {}).get("enabled", True)
        if not activo:
            est, desc = "falta", "Configurado pero apagado"
        elif nombre in PROBLEMAS:
            est, desc = PROBLEMAS[nombre]
        else:
            est, desc = "ok", "Conectado a Hermes"
        out.append({"n": "MCP: " + nombre, "est": est, "d": desc})
    return out

def grilla_real():
    """Lee la grilla de cron de verdad + como le fue en la ultima corrida.
    El panel no puede mentir: todo sale de jobs.json y executions.db.
    Devuelve {NOMBRE: {horas, agendado, estado, error, ultima_corrida}}."""
    import json as _j, sqlite3 as _s, datetime as _dt
    HOME = "/home/matiigonzz/.hermes/cron/"
    out = {}
    try:
        jobs = _j.load(open(HOME + "jobs.json", encoding="utf-8"))["jobs"]
    except Exception:
        return out

    por_job = {}
    for j in jobs:
        if not j.get("enabled"):
            continue
        partes = [x.strip() for x in str(j.get("name", "")).split("\u2014")]
        if len(partes) < 2:
            continue
        nombre = partes[1].upper()
        expr = (j.get("schedule") or {}).get("expr", "")
        campos = expr.split()
        horas = []
        if len(campos) >= 2:
            try:
                horas = sorted(int(x) for x in campos[1].split(","))
            except ValueError:
                horas = []
        out[nombre] = {
            "horas": horas,
            "agendado": True,
            "estado": j.get("last_status") or "sin correr",
            "error": (j.get("last_error") or "")[:200],
            "ultima_corrida": j.get("last_run_at"),
        }
        por_job[j.get("id")] = nombre

    # Ultimas corridas reales: un job puede figurar "ok" y haber crasheado el proceso
    try:
        con = _s.connect("file:" + HOME + "executions.db?mode=ro", uri=True)
        q = ("select job_id, status, error, started_at from executions "
             "where id in (select max(id) from executions group by job_id)")
        for job_id, estado, error, cuando in con.execute(q):
            nombre = por_job.get(job_id)
            if not nombre:
                continue
            if estado and estado not in ("completed", "done", "succeeded"):
                out[nombre]["estado"] = estado
                if error:
                    out[nombre]["error"] = str(error)[:200]
            out[nombre]["ultima_corrida"] = cuando or out[nombre]["ultima_corrida"]
        con.close()
    except Exception:
        pass
    return out

def main():
    hoy = datetime.date.today()
    REALES = grilla_real()
    agentes, tot, ult, hechos_hoy = [], 0, None, []
    for slug,(em,nm,rol,gr,pers,mod,horas,tools) in AG.items():
        d = BASE/slug
        arch = sorted(d.glob("*.md"), key=lambda p:p.stat().st_mtime, reverse=True) if d.exists() else []
        tot += len(arch)
        fecha = txt = None
        if arch:
            raw=""
            try:
                raw = arch[0].read_text(encoding="utf-8",errors="ignore"); txt = resumen(raw)
            except Exception: txt = ""
            fecha = datetime.datetime.fromtimestamp(arch[0].stat().st_mtime)
            if not ult or fecha > ult: ult = fecha
            if fecha.date() == hoy:
                hechos_hoy.append({"agente":nm,"emoji":em,"archivo":arch[0].name,
                                   "hora":fecha.strftime("%H:%M"),"que":(txt or "")[:150]})
        agentes.append({"slug":slug,"emoji":em,"nombre":nm,"rol":rol,"grupo":gr,
            "personalidad":pers,"modelo":MODELOS[mod],"horas":REALES.get(nm,{}).get("horas",[]),
            "agendado":nm in REALES,
            "cron_estado":REALES.get(nm,{}).get("estado","a pedido"),
            "cron_error":REALES.get(nm,{}).get("error",""),
            "cron_ultima":REALES.get(nm,{}).get("ultima_corrida"),
            "herramientas":tools,
            "entregables":len(arch),"ultimo_archivo":arch[0].name if arch else None,
            "ultima_fecha":fecha.strftime("%d/%m %H:%M") if fecha else None,
            "ultima_iso":fecha.isoformat() if fecha else None,
            "trabajo_hoy":bool(fecha and fecha.date()==hoy),"resumen":txt or "","_txt":raw if arch else ""})
    k = kanban()
    data = {"generado":datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "generado_iso":datetime.datetime.now().isoformat(),
        "tienda":{"marca":"GONVRA","url":"https://gonvra.com",
                  "producto":"Rasuradora Integral Recargable","precio":"$36.900"},
        "modelos":{"principal":"GPT-6 Astra (OpenAI Codex)","economico":"GPT-5.6 Sol (OpenAI Codex)",
                   "respaldo":"Kimi vía NVIDIA (Gemini quedó de última opción: lento/falla)","prohibidos":["API Next","DeepSeek"]},
        "servidor":{"host":"esta laptop","ruta":"/home/matiigonzz/Claude/gonvra2","estado":"activo","nota":"El VPS 47.85.84.11 se cayo por falta de RAM (1 GiB). Todo corre local."},
        "kanban":k,"ventas":shopify_vivo(),"herramientas":HERRAM + herramientas_locales() + automatizaciones_vivas() + mcps_reales() + [instagram_real()],"grupos":GRUPOS,"hechos_hoy":hechos_hoy,
        "totales":{"agentes":len(AG),"entregables":tot,
                   "trabajaron_hoy":sum(1 for a in agentes if a["trabajo_hoy"]),
                   "ultima_actividad":ult.strftime("%d/%m %H:%M") if ult else "—"},
        "conversacion":conversacion(agentes),"agentes":[{k:v for k,v in a.items() if k!="_txt"} for a in agentes]}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=1),encoding="utf-8")
    print(f"✅ {OUT}\n   {len(AG)} agentes · {tot} entregables · hoy: {data['totales']['trabajaron_hoy']}")

if __name__ == "__main__":
    main()
