// Prova automatica del tutor di spiegazione: simula uno studente e salva le conversazioni in un file.
// Uso: node prove/prova-tutor.mjs   (dalla cartella del repo; serve Node 18 o più recente)
import fs from "fs";

const WORKER = "https://tutor1.cristinavallini64.workers.dev/";
const LEZIONI = [[5, 1], [7, 2], [2, 1], [4, 1], [8, 0], [9, 0]];
const USCITA = "prove/conversazioni.txt";

function unita(n) {
  const h = fs.readFileSync(`studia-u${n}-index.html`, "utf8");
  const s = h.indexOf("const UNITA =") + 13;
  let d = 0, i = s;
  for (; i < h.length; i++) { if (h[i] === "{") d++; if (h[i] === "}") { d--; if (!d) break; } }
  return JSON.parse(h.slice(s, i + 1));
}

// una risposta sicuramente sbagliata, ricavata da quella giusta
function sbagliata(g, volta) {
  const p = String(g || "").trim().split(/\s+/);
  if (volta === 1) return p.length > 1 ? p.slice(1).join(" ") : "the";
  return p.length > 1 ? p.slice(0, -1).join(" ") + " to" : "a";
}

async function chiama(u, topic, messages) {
  const t0 = Date.now();
  try {
    const r = await fetch(WORKER, { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "spiega", topic, messages, unita: u, debug: true }) });
    const j = await r.json();
    return { ...j, ms: Date.now() - t0, http: r.status };
  } catch (e) { return { error: String(e), ms: Date.now() - t0 }; }
}

let out = "";
const scrivi = t => { out += t + "\n"; };
let chiamate = 0, errori = 0;

for (const [n, topic] of LEZIONI) {
  const u = unita(n);
  scrivi(`\n=== Unit ${n} · topic ${topic} (${u.topics[topic].title}) ===\n`);
  const messages = [];
  let giusta = "", stessaGiusta = "";
  const turno = async studente => {
    if (studente !== null) { messages.push({ chi: "studente", testo: studente }); scrivi(`STUDENTE: ${studente}\n`); }
    const r = await chiama(u, topic, messages); chiamate++;
    if (r.error || !r.messaggio) { errori++; scrivi(`[ERRORE ${r.http || ""}: ${r.error || "messaggio vuoto"} · ${r.ms} ms]\n`); return false; }
    messages.push({ chi: "tutor", testo: r.messaggio, risposte: r.risposte || [] });
    scrivi(`TUTOR: ${r.messaggio}\n[risposte: ${JSON.stringify(r.risposte || [])} · ${r.ms} ms]`);
    const d = (r._diag || []).filter(x => x.esercizio_scartato || x.smentita || x.errore);
    if (d.length) scrivi(`[diag: ${JSON.stringify(d)}]`);
    scrivi("");
    if (r.risposte && r.risposte.length) giusta = r.risposte[0];
    return true;
  };
  if (!(await turno(null))) continue;
  // 1 giusta · 2 sbagliata · 3 sbagliata sulla stessa frase · 4 non ho capito · 5 altra forma · 6 giusta · 7 dimmelo · 8 giusta
  await turno(giusta || "ok");
  stessaGiusta = giusta;
  await turno(sbagliata(stessaGiusta, 1));
  await turno(sbagliata(stessaGiusta, 2));
  await turno("non ho capito");
  await turno(`ma se dico ${sbagliata(stessaGiusta, 1)}?`);
  await turno(giusta || "ok");
  await turno("dimmelo");
  await turno(giusta || "ok");
}
fs.mkdirSync("prove", { recursive: true });
fs.writeFileSync(USCITA, out);
console.log(`fatto: ${chiamate} chiamate, ${errori} errori. File: ${USCITA}`);
