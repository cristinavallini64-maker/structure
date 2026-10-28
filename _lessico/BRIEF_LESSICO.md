# BRIEF — file di lessico della Structure (lessico-uN.html), Unit 2–10

Lavori in UNA sola unità, nella tua cartella `/home/claude/lex_uN/` (già pronta, con motore, script e file
della unit). Non toccare nient'altro, non fare commit, non pubblicare. Il modello completo già approvato
dall'insegnante è la Unit 1: leggi `content_u1.py` prima di cominciare, e copia stile e formato.

## Che cosa costruisci
Scrivi `content_uN.py` (stessa forma di `content_u1.py`). Poi:
    python3 build_lex.py N        # genera lessico-uN.html
    python3 check_lex.py N        # blocco A + controlli aggiuntivi: deve dire TUTTO PASS per entrambi
Ripeti finché tutto è PASS, poi fai il blocco B (sotto) e correggi. Rilancia sempre dopo ogni modifica.

In `content_uN.py`:
- `from lexlib import *` (NON impostare CFG["split_pdg"]: vale solo per la Unit 1)
- `UNIT = N`, `NAME` = titolo della unit (vedi tabella), `TOPICS` = riga di argomenti in inglese,
  `META` = breve descrizione inglese, `SK_VER = ""`, `RULE = RULE_STD`
- `LEVELS` = lista di livelli: 4–6 livelli di studio (`type="study"`, `rule=RULE`, id 1,2,3…),
  un `"rA"` (`type="review"`) a metà, un `"rB"` (`type="review"`) dopo l'ultimo studio, `"final"`
  (`type="challenge"`, titolo `★ SFIDA FINALE — <NAME>`). Titoli: `LIVELLO 01 — AREA IN INGLESE MAIUSCOLO`;
  ripassi `⟳ RIPASSO A — …` in italiano; `desc` breve in italiano.
- `GLOSS` = traduzioni italiane: parole difficili usate in definizioni e frasi + significato delle risposte.
- `STUDY` = schede di studio per OGNI livello di studio, chiavi "1","2",… uguali agli id.

## Il lessico: fonte e selezione
- Fonte: il lessico della unit (tabella sotto). Niente lessico inventato o estraneo alla unit.
- **Escludi le parole di base** che uno studente conosce già dal primo/secondo anno (es. kitchen, chair,
  football, read, weather, rain, job, teacher…). Decisione dell'insegnante: quelle parole sono inutili,
  non vanno né negli esercizi né nelle schede. Tieni solo lessico che a B1 non è scontato.
- **Escludi quello che gli Esercitati della unit insegnano come grammatica** (apri `<file esercizi>.html`,
  guarda i titoli dei livelli): es. nella Unit 1 play/do/go stanno negli Esercitati, quindi non si ripetono.
- **Dai importanza ai CHUNK** (collocazioni, espressioni fisse: make a decision, apply for a job,
  miles from anywhere…). I chunk SENZA regola si producono INTERI: la risposta è verbo + parola.

## Tipi di item (solo produzione scritta, solo fill)
- `D("«definizione inglese» → ___", "(x… y…)", "risposta", [accept])`: definizione B2 chiara, iniziali di ogni
  parola della risposta fra parentesi. Le definizioni possono chiedere anche un chunk intero.
- `G("frase con ___", "(x…)", "risposta", [accept])`: una sola `___`. Hint = iniziali delle parole della risposta.
  Per un chunk verbo + parola: hint `"(verbo + a d…)"` (il verbo NON ha iniziale: lo studente deve ricordarlo),
  e la risposta comprende il verbo nella forma che la frase richiede ("made a decision").
  Le domande fisse (Oracy, functions) si scrivono intere con le iniziali: `"(H… d… y…)"`.
- Ogni voce del livello: 1 definizione + 1 frase nel livello di studio. Ripassi e sfida: definizioni e
  frasi NUOVE (non riformulazioni a calco), mescolando D e G.
- Dimensioni indicative: 10–25 item per livello di studio, 10–16 per ripasso, 15–20 la sfida.

## Regole sugli item (blocco B, da verificare leggendo OGNI item)
1. **Risposta unica**: iniziali + contesto devono escludere sinonimi e alternative. Se un'alternativa valida
   rispetta le iniziali e il contesto, mettila in `accept` (varianti di spelling incluse: jewelry/theater,
   con/senza trattino) oppure riscrivi la frase. Mai accettare forme che annullano lo scopo dell'item.
2. **Il contesto non regala la risposta**: niente parola della stessa famiglia nella frase (es. "sail" per
   sailing, "skates" per skating), niente indizi che la rendono ovvia.
3. **Senso e naturalezza**: inglese naturale B2, frasi che hanno senso, nessuna contraddizione.
4. **Niente doppioni**: nessuna frase vicina a quelle degli Esercitati, del Cambridge, del libro (X1 lo misura),
   nessun frame ripetuto fra item (stessa struttura cambiando solo il nome).
5. **Scope grammaticale**: nelle frasi solo strutture già studiate fino a questa unit (A34 sorveglia quelle
   successive: past perfect prima della Unit 4, condizionali 2°/3° e "I wish" prima della Unit 6, passivo prima
   della Unit 9, discorso indiretto prima della Unit 10). Present perfect, futuro, present continuous,
   comparativi sono sempre leciti.
6. **Parole-spia vietate nei ripassi e nella sfida** (A42b): while, as, every, yesterday, last, at that moment,
   suddenly, any more, no longer. Nei livelli di studio usale poco.
7. **Varietà**: nomi propri vari (nessuno più di 5 volte), soggetti diversi, nessun personaggio reale.
8. **Formato**: niente virgolette dritte `"` dentro i testi (usa « » e —). Niente apostrofi tipografici nelle
   risposte (usa '). Consegne: non toccarle (vengono da lexlib).

## Schede STUDY: `[voce, definizione, esempio, italiano]` (+ `True` come quinto elemento per i chunk da coprire interi)
- `voce`: la parola o il chunk come si impara (make a decision, apply for a job, landslide).
- `definizione`: la stessa (o quasi) dell'item D. Se la voce è un chunk costruito su un nome, scrivi
  `"nome: definizione del nome"` (es. `"decision: a choice you make…"`).
- `esempio`: frase NUOVA, diversa da esercizi, Esercitati, Cambridge e libro (X2 lo misura), che CONTIENE la
  voce: la parola viene coperta in "Mettiti alla prova" (X5 verifica che si trovi). Se la definizione ha il
  prefisso "nome:", l'esempio deve contenere quel nome (anche al plurale); altrimenti la voce stessa.
  Con `True` (chunk senza regola) l'esempio deve contenere il chunk con il primo verbo eventualmente coniugato
  (makes a decision, made a decision) e le altre parole identiche.
- `italiano`: traduzione corretta, registro naturale.

## Fine lavoro
Quando `check_lex.py N` dà TUTTO PASS e hai finito il blocco B, rispondi con: numero di livelli, item, schede;
l'elenco delle voci scelte per livello; le voci della fonte che hai escluso perché di base o perché già negli
Esercitati; ogni dubbio. Non dire "tutto a posto" se non hai riletto tutto.

## Fonti del lessico per unit
| N | NAME | Esercitati | fonte |
|---|---|---|---|
| 2 | All in a day's work | present-perfect-advanced | mappa qui sotto |
| 3 | My house, my home | verb-patterns | mappa qui sotto |
| 4 | Book club | past-perfect-relatives | mappa qui sotto |
| 5 | No Planet B | first-conditional | GLOSS degli Esercitati (ricavato dalle pagine della unit) + cambridge-u5 |
| 6 | Public interest | second-conditional | idem |
| 7 | Get moving! | modals-advice | idem |
| 8 | Crime and punishment | modal-deduction | idem |
| 9 | Made to measure | passive-voice | idem |
| 10 | Watch this space! | reported-speech | idem |

Per le Unit 5–10 il glossario `const GLOSS={…}` degli Esercitati è stato costruito dalle pagine del libro:
la PRIMA parte contiene il lessico del tema della unit (es. U5: glacier, wildfire, landslide, drought…; U8:
burglar, judge, jury, witness…). Più avanti ci sono parole generiche aggiunte per le frasi degli esercizi:
quelle NON sono lessico della unit. Prendi il lessico del tema, raggruppalo per aree, aggiungi i chunk che
compaiono nelle frasi degli Esercitati e del Cambridge con quel lessico (es. "found the accused guilty",
"set fire to", "run for the council", "goes on sale").

### Unit 2 — All in a day's work (mappa del Workbook)
- jobs: scientist, beautician, app developer, vet, accountant, firefighter, police officer, lawyer, model,
  hairdresser, engineer, plumber, personal trainer, footballer, journalist, paramedic
- life and career paths: earn a good salary, take up a new hobby, do a degree, take a gap year, have children,
  get a qualification, live in the city, live by the sea, have a partner, pass an exam, fail an exam,
  get married, learn to drive, work in a team, stay single, have good friends, apply for a job, get a job,
  buy a house, be unemployed, have a career, get good marks, share a flat, retire, have an interview,
  do a course, graduate, work for a company, travel the world
- make and do: make a mistake, make an excuse, make a decision, make an appointment, make a suggestion,
  make an arrangement, make a meal, make an effort, make a cake, make a noise, make friends, make money,
  make progress, make up my mind, make the bed · do homework, do the cleaning, do the shopping,
  do the washing, do housework, do research, do my hair
  (make/do qui è LESSICO, non sta negli Esercitati: i chunk make/do si producono INTERI, verbo compreso)

### Unit 3 — My house, my home (vocabulary map p. 73 + pagine 60–79)
- rooms: attic, basement, laundry room, study, spare bedroom, hall (+ di base da escludere: kitchen, bedroom…)
- furniture: air fryer, armchair, blind, bookcase, bunk beds, carpet, chest of drawers, coffee table, cooker,
  cupboard, curtains, cushion, dishwasher, double bed, microwave, mirror, oven, rug, single bed, sink,
  wardrobe, washing machine, fireplace
- parts of a house or building: balcony, ceiling, ground floor, first floor, top floor, front door, lift,
  stairs, terrace, roof, entrance
- homes and places: bungalow, villa, cottage, terraced house, countryside, suburb, neighbourhood,
  residential area, shutters, electrical appliances, accommodation, facilities, houseplant, strings of lights
- Real talk: miles from anywhere, nothing fancy, low-tech, come round, alright for some, we'll see
- describing places: not far from, ten minutes' walk from, a long way from, compared to, on the other hand,
  whereas

### Unit 4 — Book club (vocabulary map p. 93)
- adjectives: average, awful, believable, charming, confusing, cruel, disappointing, easy-to-read, enjoyable,
  evil, funny, informative, kind, realistic, strong, terrible, terrific, terrifying, tragic, weak
- kinds of books: comic book, crime novel, fantasy novel, graphic novel, historical novel, horror story,
  romantic novel, science fiction, short story, thriller, autobiography, biography, cookbook, history book,
  travel book
- parts of a story: beginning, chapter, character, ending, hero, heroine, illustration, plot, set in, theme,
  title, villain
- people: author, blogger, novelist (+ publisher, bestseller, page-turner, trilogy, review dalle pagine)
