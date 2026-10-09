// Controllo del tutor di spiegazione dopo ogni modifica.
// 1) APERTURE: il primo messaggio di OGNI argomento di OGNI unità (quello che lo studente vede appena apre).
// 2) CASI GIÀ RISOLTI: le situazioni che erano sbagliate e sono state corrette, per vedere che non tornino.
// Uso: node prove/controllo.mjs   → scrive prove/controllo.txt
import fs from "fs";

const WORKER = "https://tutor1.cristinavallini64.workers.dev/";
const USCITA = "prove/controllo.txt";

function unita(n) {
  const h = fs.readFileSync(`studia-u${n}-index.html`, "utf8");
  const s = h.indexOf("const UNITA =") + 13;
  let d = 0, i = s;
  for (; i < h.length; i++) { if (h[i] === "{") d++; if (h[i] === "}") { d--; if (!d) break; } }
  return JSON.parse(h.slice(s, i + 1));
}
const pausa = ms => new Promise(r => setTimeout(r, ms));
async function chiama(u, topic, messages) {
  const t0 = Date.now();
  for (let k = 0; k < 2; k++) {
    try {
      const r = await fetch(WORKER, { method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "spiega", topic, messages, unita: u, debug: true }) });
      const j = await r.json();
      if (!j.error || k === 1) return { ...j, ms: Date.now() - t0 };
    } catch (e) { if (k === 1) return { error: String(e), ms: Date.now() - t0 }; }
    await pausa(3000);
  }
}

let out = "";
const scrivi = t => { out += t + "\n"; };
const avvisi = [];
const diagUtile = r => (r._diag || []).filter(x => x.esercizio_scartato || x.smentita || x.troppo_lungo);

// controlli automatici sul messaggio del tutor
function controlla(dove, r) {
  const m = String(r.messaggio || "");
  const spazi = (m.match(/___/g) || []).length;
  if (r.error) avvisi.push(`${dove}: ERRORE ${r.error}`);
  if (m.length > 650) avvisi.push(`${dove}: messaggio lungo (${m.length} caratteri)`);
  if (spazi > 1) avvisi.push(`${dove}: ${spazi} spazi ___ nello stesso messaggio`);
  if (/`/.test(m)) avvisi.push(`${dove}: apici inversi`);
  if (/\b(bravo|bravissimo|attento)\b/i.test(m)) avvisi.push(`${dove}: maschile`);
  if (spazi === 1 && !(r.risposte || []).length) avvisi.push(`${dove}: frase da completare senza risposte`);
}

// 1) APERTURE
scrivi("########## 1) APERTURE: primo messaggio di ogni argomento ##########");
for (let n = 1; n <= 10; n++) {
  const u = unita(n);
  for (let t = 0; t < u.topics.length; t++) {
    const r = await chiama(u, t, []);
    const dove = `U${n} T${t} (${u.topics[t].title})`;
    controlla(dove, r);
    scrivi(`\n=== ${dove} · ${r.ms} ms ===\n${r.error ? "ERRORE: " + r.error : r.messaggio}\n[risposte: ${JSON.stringify(r.risposte || [])}]`);
    const d = diagUtile(r); if (d.length) scrivi(`[diag: ${JSON.stringify(d)}]`);
  }
}

// 2) CASI GIÀ RISOLTI: conversazione preparata + messaggio dello studente
const CASI = [
  { nome: "will → would: deve spiegare con un esempio, non fare domande", n: 10, t: 0,
    tutor: "Ora prova tu:\n« I'll text you. » → Pietro said that he ___ me.", risposte: ["would text", "'d text"], studente: "non so come trasformare will" },
  { nome: "it has rained: non deve dire che è un'azione conclusa (quello è il past simple)", n: 2, t: 1,
    tutor: "Prova tu:\nLook outside! It ___ (rain) since this morning.", risposte: ["has been raining"], studente: "ma se io dico it has rained?" },
  { nome: "unless giusto: deve dire Esatto", n: 5, t: 1,
    tutor: "Prova tu:\nI will fail the exam ___ I study hard.", risposte: ["unless"], studente: "unless" },
  { nome: "risposta giusta (up): deve dire Esatto", n: 7, t: 2,
    tutor: "Prova tu:\nEvery day, my brother wakes ___ at 7 o'clock.", risposte: ["up"], studente: "up" },
  { nome: "dimmelo: deve dare la risposta", n: 8, t: 0,
    tutor: "Zeno vede il vicino in giardino con la vanga.\nHe ___ (work) in the garden.", risposte: ["must be working"], studente: "dimmelo" },
  { nome: "risposta sbagliata: non deve dire la parola giusta né la forma", n: 3, t: 1,
    tutor: "Prova tu:\nI was running, so I stopped ___ (drink) some water.", risposte: ["to drink"], studente: "drinking" },
  { nome: "domanda di passivo: lo spazio deve contenere verbo e soggetto", n: 9, t: 0,
    tutor: "Bene. Ora una domanda: come chiedi se il latte viene aggiunto alla miscela?", risposte: [], studente: "ok" },
  { nome: "domanda dello studente: deve rispondere davvero, senza rimandare", n: 1, t: 3,
    tutor: "Prova tu:\nAs Marta opened the door, the lights ___ (go) out.", risposte: ["went"], studente: "ma as non vuol dire man mano?" },
];
scrivi("\n\n########## 2) CASI GIÀ RISOLTI ##########");
for (const c of CASI) {
  const u = unita(c.n);
  const r = await chiama(u, c.t, [{ chi: "tutor", testo: c.tutor, risposte: c.risposte }, { chi: "studente", testo: c.studente }]);
  controlla(c.nome, r);
  scrivi(`\n=== ${c.nome} (U${c.n} T${c.t}) · ${r.ms} ms ===\nTUTOR (prima): ${c.tutor}\nSTUDENTE: ${c.studente}\nTUTOR: ${r.error ? "ERRORE: " + r.error : r.messaggio}\n[risposte: ${JSON.stringify(r.risposte || [])}]`);
  const d = diagUtile(r); if (d.length) scrivi(`[diag: ${JSON.stringify(d)}]`);
}

scrivi("\n\n########## AVVISI AUTOMATICI ##########\n" + (avvisi.length ? avvisi.join("\n") : "nessuno"));
fs.writeFileSync(USCITA, out);
console.log(`fatto: ${avvisi.length} avvisi automatici. File: ${USCITA}`);
