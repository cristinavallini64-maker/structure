#!/usr/bin/env python3
# Costruisce lessico-u1.html (The Structure, Unit 1 "Use your time!") dal motore di
# past-narrative.html. Fonte autorevole dei contenuti: questo script.
# Due tipi di item, entrambi di produzione scritta, niente traduzione dall'italiano:
#   DEF  = definizione inglese -> parola (iniziali come ancora)
#   GAP  = frase con buco -> verbo + attivita' (collocazione), iniziale dell'attivita'
import json, re, sys, importlib
N = int(sys.argv[1])
C = importlib.import_module("content_u%d" % N)
LEVELS, GLOSS, STUDY = C.LEVELS, C.GLOSS, C.STUDY
TPL = "past-narrative.html"
OUT = "lessico-u%d.html" % N
from lexlib import I_DEF
# ------------------------------------------------------------------------ render
def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def item_js(it):
    if it[0] == "def":
        _, q, hint, a, acc = it
        ins, badge = I_DEF, "// DEFINIZIONE"
    else:
        _, q, hint, a, acc, ins = it
        badge = "// COMPLETA LA FRASE"
    if '"' in q or '"' in a:
        sys.exit("virgolette dritte non ammesse: " + q)
    accs = ",".join('"%s"' % esc(x) for x in acc)
    return ('{type:"fill",q:"%s",hint:"%s",a:"%s",accept:[%s],instruction:"%s",badge:"%s"}'
            % (esc(q), esc(hint), esc(a), accs, esc(ins), badge))

out = ["const LEVELS=["]
for L in LEVELS:
    lid = L["id"] if isinstance(L["id"], int) else '"%s"' % L["id"]
    head = '{id:%s,type:"%s",title:"%s",desc:"%s",' % (lid, L["type"], L["title"], L["desc"])
    if L.get("rule"):
        head += "\nrule:`%s`," % L["rule"]
    out.append(head)
    out.append("exercises:[")
    out.append(",\n".join(item_js(i) for i in L["items"]))
    out.append("]},")
out[-1] = out[-1].rstrip(",")
out.append("];\n")
LEV_JS = "\n".join(out)

# ------------------------------------------------------------------ studio
CSS_STUDY = """
.btn-studia{margin-top:9px;font-family:'Space Grotesk',sans-serif;font-size:11px;font-weight:700;letter-spacing:.5px;padding:6px 12px;border-radius:8px;cursor:pointer;border:1.5px solid var(--plum);background:rgba(122,59,143,.08);color:var(--plum2);}
.btn-studia:hover{background:rgba(122,59,143,.16);}
.st-tools{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px;}
.st-list{display:flex;flex-direction:column;gap:10px;}
.st-card{background:var(--paper2);border:1px solid var(--line);border-left:3px solid var(--plum);border-radius:0 var(--rs) var(--rs) 0;padding:12px 15px;}
.st-word{font-family:'Sora',sans-serif;font-weight:800;font-size:17px;color:var(--ink);}
.st-key{font:inherit;font-weight:700;color:var(--plum2);}\n.st-def .st-key{font-weight:inherit;color:inherit;}
.st-it{font-size:13px;color:var(--plum2);font-weight:600;margin-left:6px;}
.st-def{font-size:14px;color:var(--sub);margin-top:4px;}
.st-ex{font-size:14px;color:var(--ink);font-style:italic;margin-top:5px;}
.st-quiz .st-word,.st-quiz .st-it{filter:blur(7px);user-select:none;cursor:pointer;}
.st-quiz .st-card.show .st-word,.st-quiz .st-card.show .st-it{filter:none;}
.st-hint{font-size:12px;color:var(--mut);margin-bottom:10px;}
"""
HTML_STUDY = """<div id="screen-study" class="screen">
  <div class="ex-header">
    <div class="ex-title" id="stTitle"></div>
    <button class="btn-back" onclick="goMap()">← Mappa</button>
  </div>
  <div class="st-tools">
    <button class="btn btn-secondary" id="stQuizBtn" onclick="toggleQuiz()">Mettiti alla prova</button>
    <button class="btn btn-primary" id="stGoBtn">Vai agli esercizi →</button>
  </div>
  <div class="st-hint" id="stHint"></div>
  <div class="st-list" id="stList"></div>
</div>
"""
JS_STUDY = r"""
function openStudy(id){
  const lv=LEVELS.find(l=>String(l.id)===String(id));const rows=STUDY[String(id)]||[];
  document.getElementById('stTitle').textContent=lv.title.replace(/^LIVELLO/,'STUDIA ·');
  const list=document.getElementById('stList');list.classList.remove('st-quiz');
  document.getElementById('stQuizBtn').textContent='Mettiti alla prova';
  document.getElementById('stHint').textContent='Leggi la parola, la definizione e l\u2019esempio. Poi prova a coprire le parole.';
  list.innerHTML=rows.map(r=>{
    const m=r[1].match(/^([^:]+):\s*(.*)$/);const key=m?m[1]:r[0].replace(/[\u2026?]+$/,'');
    const def=m?`<span class="st-word st-key">${m[1]}:</span> ${m[2]}`:r[1];
    const esc=x=>x.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    const CH=r[4]===true;
    const rx=CH?new RegExp('\\b'+r[0].split(' ').map((w,i)=>i?esc(w):esc(w)+'\\w*').join('\\s+'),'gi'):new RegExp('\\b('+esc(key)+')\\w*','gi');
    const ex=r[2].replace(rx,w=>`<span class="st-word st-key">${w}</span>`);
    return `<div class="st-card" onclick="this.classList.toggle('show')"><div><span class="st-word">${r[0]}</span><span class="st-it">${r[3]}</span></div><div class="st-def">${def}</div><div class="st-ex">${ex}</div></div>`;}).join('');
  document.getElementById('stGoBtn').onclick=()=>openLevel(lv);
  showScreen('study');window.scrollTo(0,0);
}
function toggleQuiz(){
  const list=document.getElementById('stList');const on=list.classList.toggle('st-quiz');
  list.querySelectorAll('.st-card').forEach(c=>c.classList.remove('show'));
  document.getElementById('stQuizBtn').textContent=on?'Mostra tutto':'Mettiti alla prova';
  document.getElementById('stHint').textContent=on?'Leggi definizione ed esempio, d\u00ec la parola, poi tocca la scheda per controllare.':'Leggi la parola, la definizione e l\u2019esempio. Poi prova a coprire le parole.';
}
"""

s = open(TPL, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"sostituzione attesa {count} volta/e, trovata {n}: {old[:60]!r}")
    s = s.replace(old, new)

rep("<title>Unit 1 · Past Narrative — Grammar Practice (B2)</title>",
    "<title>Unit %d · %s — Vocabulary Practice (B2)</title>" % (N, C.NAME))
rep(re.search(r'<meta name="description" content="[^"]*">', s).group(0),
    '<meta name="description" content="The Structure · Lessico Unit %d %s: %s. Definizioni in inglese e chunk. Preparazione B2 First.">' % (N, C.NAME, C.META))
rep('<div><div class="logo">Unit 1 · Past Narrative</div><span class="logo-sub">grammar practice · B2</span></div>',
    '<div><div class="logo">Unit %d · Lessico</div><span class="logo-sub">vocabulary practice · B2</span></div>' % N)
rep("<h2>The Structure · Practice</h2>", "<h2>The Structure · Lessico</h2>")
rep("<h1>Use your time!</h1>", "<h1>%s</h1>" % C.NAME)
rep("<p>used to · past continuous · past simple · when/while/as · adverbs of sequence</p>",
    "<p>%s</p>" % C.TOPICS)
# glossario
g0 = s.index("const GLOSS={"); g1 = s.index("\n", g0)
s = s[:g0] + "const GLOSS=" + json.dumps(GLOSS, ensure_ascii=False, separators=(",", ":")) + s[g1:]
# livelli
l0 = s.index("const LEVELS=["); l1 = s.index("const SK=")
s = s[:l0] + LEV_JS + "\n" + s[l1:]
rep("const SK='gq_u1pn_s',EK='gq_u1pn_e';", "const SK='lex_s_u%d%s_s',EK='lex_s_u%d%s_e';" % (N, C.SK_VER, N, C.SK_VER))
rep("return 'GQU.'+b64;", "return 'LXU%d.'+b64;" % N)
rep('<div class="cb-title">GRAMMAR MASTER!</div>', '<div class="cb-title">VOCABULARY MASTER!</div>')
rep("hai completato tutta la Unit 1 &middot; missione compiuta", "hai completato tutto il lessico della Unit %d &middot; missione compiuta" % N)
rep('<div class="ex-type-badge">// FILL IN THE BLANK</div>', '<div class="ex-type-badge">${ex.badge||\'// FILL IN THE BLANK\'}</div>')

rep("</style>", CSS_STUDY + "</style>")
s = s.replace("#screen-map,#screen-exercise,#screen-results{", "#screen-map,#screen-exercise,#screen-study,#screen-results{")
rep('<div id="screen-results" class="screen"></div>', HTML_STUDY + '<div id="screen-results" class="screen"></div>')
rep("const LEVELS=[", "const STUDY=" + json.dumps(STUDY, ensure_ascii=False) + ";\n" + JS_STUDY + "const LEVELS=[")
rep('<div class="sc-desc">${s.desc}</div></div>${badge}', '<div class="sc-desc">${s.desc}</div>${STUDY[String(s.id)]?`<button class="btn-studia" onclick="event.stopPropagation();openStudy(\'${s.id}\')">&#x1F4D6; Studia le parole</button>`:\'\'}</div>${badge}')
open(OUT, "w", encoding="utf-8").write(s)
n = sum(len(L["items"]) for L in LEVELS)
print(f"{OUT}: {len(LEVELS)} livelli, {n} item")
for L in LEVELS: print(f"   {L['id']}: {len(L['items'])}")
