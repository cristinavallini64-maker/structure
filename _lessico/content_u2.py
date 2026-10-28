# Contenuti del lessico, Unit 2 "All in a day's work"
from lexlib import *
UNIT = 2
NAME = "All in a day's work"
TOPICS = "jobs · studies and qualifications · work and career · make and do · life choices and housework"
META = "jobs, studies, careers, make and do collocations, life choices and housework"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — JOBS",
 desc="mestieri e professioni", rule=RULE, items=[
 D("«a person whose job is to give treatments to the face, skin and nails, for example in a salon» → ___", "(b…)", "beautician"),
 D("«a person who designs and writes the programs that people download on their phones» → ___", "(a… d…)", "app developer"),
 D("«a person whose job is to keep and check the financial records of a company or a person, and to prepare tax documents» → ___", "(a…)", "accountant"),
 D("«a person who gives legal advice and represents people in court» → ___", "(l…)", "lawyer"),
 D("«a person who fits and repairs water pipes, taps, toilets and boilers» → ___", "(p…)", "plumber"),
 D("«a fitness expert who plans exercises for one client at a time and checks their progress» → ___", "(p… t…)", "personal trainer"),
 D("«a person who collects news and writes articles or reports for newspapers, TV or websites» → ___", "(j…)", "journalist"),
 D("«a person trained to give emergency help to sick or injured people, usually in an ambulance» → ___", "(p…)", "paramedic"),
 G("Before her sister's wedding, Marta booked a ___ to do her nails and eyebrows at home.", "(b…)", "beautician"),
 G("Kevin taught himself to code, created a phone game in his bedroom, and now works as an ___ for a start-up.", "(a… d…)", "app developer"),
 G("Each spring Grandma takes a box of receipts to her ___, who fills in her tax forms.", "(a…)", "accountant"),
 G("After the car accident, Omar hired a ___ to take the other driver to court.", "(l…)", "lawyer"),
 G("Water is coming through the kitchen ceiling — call a ___ before it gets worse!", "(p…)", "plumber"),
 G("Three times a week Elena meets her ___ at the gym; he has given her a new set of exercises for her back.", "(p… t…)", "personal trainer"),
 G("A ___ from the local paper has interviewed our headteacher about the new science lab.", "(j…)", "journalist"),
 G("The ambulance arrived in eight minutes, and two ___ gave the injured cyclist oxygen on the pavement.", "(p…)", "paramedics"),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — STUDIES AND QUALIFICATIONS",
 desc="laurea, corsi, esami, voti · anno sabbatico", rule=RULE, items=[
 D("«to study at university for three or more years in a subject such as law or physics» → ___", "(d… a d…)", "do a degree"),
 D("«to attend a series of lessons on one subject, for example in the evenings or online» → ___", "(d… a c…)", "do a course"),
 D("«to study a subject carefully to discover new facts, for example in a laboratory» → ___", "(d… r…)", "do research"),
 D("«to obtain an official certificate that shows you have the skills for a job» → ___", "(g… a q…)", "get a qualification", ["get a qualification","gain a qualification"]),
 D("«to be successful in an important test» → ___", "(p… an e…)", "pass an exam"),
 D("«to not reach the minimum score in an important test, so you need to take it again» → ___", "(f… an e…)", "fail an exam"),
 D("«to receive high scores for your schoolwork and tests» → ___", "(g… g… m…)", "get good marks"),
 D("«to finish your university studies and receive your diploma» → ___", "(g…)", "graduate"),
 D("«to spend twelve months travelling or working between school and university» → ___", "(t… a g… y…)", "take a gap year"),
 G("My cousin ___ in civil engineering at Padua; she's in her second year now.", "(verbo + a d…)", "is doing a degree", ["is doing a degree","is taking a degree"]),
 G("Before he opened his café, Yusuf ___ in coffee-making; it lasted six weeks and cost three hundred euros.", "(verbo + a c…)", "did a course", ["did a course","took a course","attended a course"]),
 G("Dr Bassi ___ on bees at the university; she wants to find out why so many of them are dying.", "(verbo + r…)", "does research", ["does research","is doing research","conducts research"]),
 G("You can't work in a hospital laboratory without the right papers, so Luca needs to ___ first.", "(verbo + a q…)", "get a qualification", ["get a qualification","gain a qualification","obtain a qualification","earn a qualification"]),
 G("Wanda studied anatomy for months, and today she ___ with twenty-eight out of thirty.", "(verbo + the e…)", "passed the exam", ["passed the exam","has passed the exam"]),
 G("Nobody can believe it: Greta ___ again — that's the third one this year!", "(verbo + an e…)", "has failed an exam", ["has failed an exam","failed an exam"]),
 G("Lorenzo studies hard and always ___ in physics: nothing below eight.", "(verbo + g… m…)", "gets good marks"),
 G("Chiara has nearly finished her law studies: she'll ___ in March, after five long years.", "(g…)", "graduate"),
 G("Before university, Samir wants to ___ and work on a farm in New Zealand.", "(verbo + a g… y…)", "take a gap year", ["take a gap year","have a gap year","spend a gap year"]),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — WORK AND CAREER",
 desc="cercare lavoro, colloqui, stipendio · disoccupazione e pensione", rule=RULE, items=[
 D("«to ask formally for a position at work, usually by sending a CV and a letter» → ___", "(a… for a j…)", "apply for a job"),
 D("«to meet an employer who asks you questions to decide if you are right for a job» → ___", "(h… an i…)", "have an interview"),
 D("«to be an employee of a business» → ___", "(w… for a c…)", "work for a company"),
 D("«to do your job together with a group of colleagues» → ___", "(w… in a t…)", "work in a team"),
 D("«to receive a lot of money for the work you do» → ___", "(e… a g… s…)", "earn a good salary"),
 D("«to get money, for example from a job or by selling things» → ___", "(m… m…)", "make money"),
 D("«to do a series of jobs in one area over many years, reaching better positions» → ___", "(h… a c…)", "have a career"),
 D("«without a paid job, but wanting one» → ___", "(u…)", "unemployed"),
 D("«to stop working because you have reached a certain age» → ___", "(r…)", "retire"),
 G("Mattia has seen an advert for a waiter at the hotel, and he wants to ___ there. He's writing his CV now.", "(verbo + for a j…)", "apply for a job"),
 G("Wish me luck! I ___ at the bank at nine tomorrow, and I'm really nervous.", "(verbo + an i…)", "have an interview", ["have an interview","have got an interview","am having an interview","'ve got an interview","'m having an interview"]),
 G("Since 2019 Ada ___ that produces solar panels; she manages the sales team.", "(verbo + for a c…)", "has worked for a company", ["has worked for a company","has been working for a company"]),
 G("Nobody at the agency has a project of their own: we ___ of five, and we share all the ideas.", "(verbo + in a t…)", "work in a team"),
 G("Pilots ___, but they spend many nights away from home.", "(verbo + a g… s…)", "earn a good salary", ["earn a good salary","get a good salary","make a good salary","have a good salary"]),
 G("At fifteen Bruno started to ___ by selling his old comics online.", "(verbo + m…)", "make money", ["make money","earn money"]),
 G("Ilaria dreams of a life on the stage: she wants to ___ in the theatre.", "(verbo + a c…)", "have a career", ["have a career","build a career","pursue a career"]),
 G("When the shoe factory closed, two hundred workers found themselves ___.", "(u…)", "unemployed"),
 G("After forty-two years on the trains, Mr Ferri is going to ___ in June and spend more time in his garden.", "(r…)", "retire"),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — mestieri, studi, lavoro",
 desc="i primi tre livelli insieme · frasi e definizioni nuove", items=[
 D("«someone who looks after people's skin, nails and make-up in a salon» → ___", "(b…)", "beautician"),
 G("Our boiler has broken down again; the ___ is coming at four to fix it.", "(p…)", "plumber"),
 G("The court case went on for two years, and Mr Ricci paid his ___ more than ten thousand euros.", "(l…)", "lawyer"),
 D("«a professional who prepares tax forms and checks the money that a business spends and receives» → ___", "(a…)", "accountant"),
 G("Federica sent her CV to six hotels in May, and in June she ___ with the manager of the biggest one.", "(verbo + an i…)", "had an interview"),
 G("I want to ___ at the new shopping centre; they need shop assistants for Christmas.", "(verbo + for a j…)", "apply for a job"),
 D("«to complete a university course successfully» → ___", "(g…)", "graduate"),
 G("All those weeks of revision paid off: Zoe ___ with the top score in the class.", "(verbo + the e…)", "passed the exam", ["passed the exam","has passed the exam"]),
 G("Most of my friends want to start university straight away, but Pablo prefers to ___ and volunteer in Peru first.", "(verbo + a g… y…)", "take a gap year", ["take a gap year","have a gap year","spend a gap year"]),
 D("«having no job, although you are able and ready to work» → ___", "(u…)", "unemployed"),
 G("Software engineers in big cities often ___, but rents there are very high too.", "(verbo + a g… s…)", "earn a good salary", ["earn a good salary","get a good salary","make a good salary","have a good salary"]),
 G("Mr Lodi is sixty-seven and still runs his shop; he doesn't want to ___ yet.", "(r…)", "retire"),
 G("Agnese is good at listening and sharing ideas, so she's happy to ___ at the architecture firm.", "(verbo + in a t…)", "work in a team"),
 G("Alessio ___ in medicine at Bologna; it takes six years.", "(verbo + a d…)", "is doing a degree", ["is doing a degree","is taking a degree"]),
 G("A ___ helped my dad lose twelve kilos with a programme of exercises just for him.", "(p… t…)", "personal trainer"),
 D("«someone who creates software for smartphones and tablets» → ___", "(a… d…)", "app developer"),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — MAKE: DECISIONS AND PLANS",
 desc="decidere, proporre, prendere accordi e appuntamenti", rule=RULE, items=[
 D("«to choose what to do after thinking about it» → ___", "(m… a d…)", "make a decision"),
 D("«to decide, especially after a period of doubt» → ___", "(m… up my m…)", "make up my mind"),
 D("«to give an idea for other people to think about» → ___", "(m… a s…)", "make a suggestion"),
 D("«to agree a plan with another person, for example about who does what or where to meet» → ___", "(m… an a…)", "make an arrangement"),
 D("«to fix a time to see a doctor, a dentist or another professional» → ___", "(m… an a…)", "make an appointment"),
 G("Choosing a university is hard, and Rita has to ___ by Friday.", "(verbo + a d…)", "make a decision", ["make a decision","take a decision"]),
 G("Kim can't ___: the red jacket or the green one? She's been in the shop for an hour.", "(verbo + up her m…)", "make up her mind"),
 G("At the meeting nobody spoke for a long time, so Fatima ___: a cake sale to raise money for the trip.", "(verbo + a s…)", "made a suggestion"),
 G("I've ___ with my neighbour: she's feeding the cat until I'm back from Spain.", "(verbo + an a…)", "made an arrangement", ["made an arrangement","made an agreement"]),
 G("My tooth hurts: I need to phone the dentist and ___ for this week.", "(verbo + an a…)", "make an appointment", ["make an appointment","book an appointment"]),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — MAKE: EFFORT AND MISTAKES",
 desc="errori, scuse, impegno, progressi · rumore e amicizie", rule=RULE, items=[
 D("«to do something wrong without wanting to» → ___", "(m… a m…)", "make a mistake"),
 D("«to give a reason, often not true, to explain why you can't do something» → ___", "(m… an e…)", "make an excuse"),
 D("«to try hard to do something» → ___", "(m… an e…)", "make an effort"),
 D("«to improve or move forward towards a goal» → ___", "(m… p…)", "make progress"),
 D("«to produce a sound, often an unwanted one» → ___", "(m… a n…)", "make a noise"),
 D("«to meet new people and start relationships of trust with them» → ___", "(m… f…)", "make friends"),
 G("Check your answers again: you ___ in question three — it's «went», not «goed».", "(verbo + a m…)", "made a mistake", ["made a mistake","have made a mistake"]),
 G("When it's his turn to wash up, Ivan always ___ — a headache, homework, an urgent phone call.", "(verbo + an e…)", "makes an excuse", ["makes an excuse","finds an excuse"]),
 G("Nina has never liked maths, but this year she's ___, and her marks are better.", "(verbo + an e…)", "making an effort", ["making an effort","made an effort"]),
 G("After three months of lessons, Bianca ___ with the violin: she can play a simple tune now.", "(verbo + p…)", "has made progress", ["has made progress","is making progress"]),
 G("I heard someone downstairs, so I went down very slowly, trying not to ___.", "(verbo + a n…)", "make a noise"),
 G("At first the new school was hard for Ahmed, but he ___ quickly, and now he's never alone at break.", "(verbo + f…)", "made friends"),
]))

# ---------------------------------------------------------------- 06
LEVELS.append(dict(id=6, type="study", title="LIVELLO 06 — LIFE CHOICES AND HOUSEWORK",
 desc="scelte di vita · do: pulizie, bucato, lavori di casa", rule=RULE, items=[
 D("«to live in an apartment with other people and divide the rent and the bills» → ___", "(s… a f…)", "share a flat"),
 D("«to not get married or have a partner» → ___", "(s… s…)", "stay single"),
 D("«to start an activity for fun that you didn't do before» → ___", "(t… up a n… h…)", "take up a new hobby"),
 D("«to make the house tidy and free of dust and dirt» → ___", "(d… the c…)", "do the cleaning"),
 D("«to wash clothes, usually in a machine» → ___", "(d… the w…)", "do the washing"),
 D("«to do jobs at home such as ironing, dusting and washing up» → ___", "(d… h…)", "do housework"),
 D("«to wash, brush and style your own hair» → ___", "(d… my h…)", "do my hair"),
 G("Two students, one small kitchen and lots of arguments about the dishes: that's life when you ___ with a friend.", "(verbo + a f…)", "share a flat"),
 G("Aunt Paola has never wanted a husband; she prefers to ___ and travel the world alone.", "(verbo + s…)", "stay single", ["stay single","remain single"]),
 G("Bored at home in winter, Valeria ___: she's learning to knit.", "(verbo + up a n… h…)", "took up a new hobby", ["took up a new hobby","has taken up a new hobby","picked up a new hobby"]),
 G("In our house Dad ___ on Saturday mornings: floors, bathroom, windows.", "(verbo + the c…)", "does the cleaning"),
 G("There are no clean socks in the drawer — somebody needs to ___ today.", "(verbo + the w…)", "do the washing"),
 G("My grandfather never ___ when he was young; now he irons his own shirts.", "(verbo + h…)", "did housework", ["did housework","did the housework"]),
 G("I want curls and a plait for the party, so I need ten more minutes to ___.", "(verbo + my h…)", "do my hair", ["do my hair","style my hair"]),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — make, do e scelte di vita",
 desc="livelli 4-6 e qualcosa di prima · frasi e definizioni nuove", items=[
 G("You can't have both, Marco — you need to ___: the drama club or the football team?", "(verbo + a d…)", "make a decision", ["make a decision","take a decision"]),
 D("«to book a meeting with a doctor, a lawyer or a hairdresser» → ___", "(m… an a…)", "make an appointment"),
 G("I can't ___ about the trip: it's expensive, but all my friends are going.", "(verbo + up my m…)", "make up my mind"),
 G("Ssh! Don't ___ — Grandpa is having a nap on the sofa.", "(verbo + a n…)", "make a noise"),
 D("«to invent a reason so that you don't have to do something» → ___", "(m… an e…)", "make an excuse"),
 G("Sara finds her new classmates boring, but her mum wants her to ___ to be friendly.", "(verbo + an e…)", "make an effort"),
 G("I ___ in my email: I wrote «Dear Sir» to a woman.", "(verbo + a m…)", "made a mistake", ["made a mistake","have made a mistake"]),
 G("Since October our robotics team ___: now the robot can climb stairs.", "(verbo + p…)", "has made progress", ["has made progress","has been making progress"]),
 G("Can I ___? Why don't we take the train? It's cheaper than petrol.", "(verbo + a s…)", "make a suggestion"),
 G("My sister and I have ___: she takes the car on weekdays, and I have it at weekends.", "(verbo + an a…)", "made an arrangement", ["made an arrangement","made an agreement"]),
 G("Since September Noemi ___ with two nursing students near the hospital.", "(verbo + a f…)", "has shared a flat", ["has shared a flat","has been sharing a flat"]),
 G("Ettore is forty and lives happily on his own: marriage isn't for him, and he plans to ___.", "(verbo + s…)", "stay single", ["stay single","remain single"]),
 D("«to begin a new activity in your free time, for example painting or knitting» → ___", "(t… up a n… h…)", "take up a new hobby"),
 G("The machine is full of wet clothes — who ___ this morning and forgot to hang them out?", "(verbo + the w…)", "did the washing"),
 G("In our flat we take turns to ___: I vacuum and dust, and my flatmate scrubs the bathroom.", "(verbo + the c…)", "do the cleaning"),
 G("The ___ put a bandage on the boy's head and drove him to hospital with the siren on.", "(p…)", "paramedic"),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — All in a day's work",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 D("«a professional who repairs leaking taps and blocked toilets» → ___", "(p…)", "plumber"),
 G("Lisa's job is to design phone programs: she's an ___ at a start-up in Milan.", "(a… d…)", "app developer"),
 G("My aunt is a ___: she defends people in court and spends her evenings reading old cases.", "(l…)", "lawyer"),
 G("Ugo is ___ in history at Ca' Foscari, and he wants to teach.", "(verbo + a d…)", "doing a degree", ["doing a degree","taking a degree"]),
 D("«to stop working for good, usually at the age of sixty-five or more» → ___", "(r…)", "retire"),
 G("Diego didn't open his chemistry book once, and he ___: he has to take it again after the summer.", "(verbo + the e…)", "failed the exam", ["failed the exam","has failed the exam"]),
 G("My parents ___ at the bank: they want to ask for a loan for a bigger flat.", "(verbo + an a…)", "have made an appointment", ["have made an appointment","have booked an appointment","made an appointment","booked an appointment"]),
 G("It's hard to ___ in a new city, but joining a sports club helps.", "(verbo + f…)", "make friends"),
 G("We ___ about the holiday: Greece, not Spain. Final answer!", "(verbo + a d…)", "have made a decision", ["have made a decision","made a decision","have taken a decision","took a decision"]),
 D("«a health worker who arrives with the siren on and treats the victims of road accidents» → ___", "(p…)", "paramedic"),
 G("Gianni wants to ___ in sports reporting, so he writes for the school magazine and a local website.", "(verbo + a c…)", "have a career", ["have a career","build a career","pursue a career"]),
 G("Agata ___ with her café: she sells vegan cakes, and the place is always full.", "(verbo + m…)", "makes money", ["makes money","earns money"]),
 G("Our English teacher wants us to ___ with our pronunciation, so we record ourselves on the phone.", "(verbo + p…)", "make progress"),
 G("This spring Mum ___: she keeps bees in the garden now.", "(verbo + up a n… h…)", "took up a new hobby", ["took up a new hobby","has taken up a new hobby","picked up a new hobby"]),
 G("Don't ___, Paolo — just say you forgot my birthday.", "(verbo + an e…)", "make an excuse"),
 G("My brother never helps at home: Mum ___ alone, from the ironing to the dusting.", "(verbo + h…)", "does housework", ["does housework","does the housework"]),
 D("«a coach who helps clients get fit with exercise plans just for them» → ___", "(p… t…)", "personal trainer"),
 G("Elisa spent an hour with pins and a curling iron to ___ for her cousin's wedding.", "(verbo + her h…)", "do her hair", ["do her hair","style her hair"]),
 D("«to finish a training course successfully and receive a diploma that lets you work in a profession» → ___", "(g… a q…)", "get a qualification", ["get a qualification","gain a qualification"]),
 G("Ivo wants to ___ that designs video games; he loves big projects with lots of people.", "(verbo + for a c…)", "work for a company"),
]))

# glossa: parole difficili delle definizioni e delle frasi + significato delle risposte
GLOSS = {
 "beautician":"estetista","app developer":"sviluppatore di app","accountant":"commercialista, contabile",
 "lawyer":"avvocato","plumber":"idraulico","personal trainer":"allenatore personale","journalist":"giornalista",
 "paramedic":"paramedico, soccorritore","paramedics":"paramedici, soccorritori",
 "treatments":"trattamenti","salon":"salone, centro estetico","eyebrows":"sopracciglia","nails":"unghie",
 "financial records":"documenti contabili","receipts":"ricevute, scontrini","tax":"tasse","legal advice":"consulenza legale",
 "court":"tribunale","pipes":"tubi","taps":"rubinetti","boilers":"caldaie","boiler":"caldaia","leaking":"che perdono",
 "blocked":"intasati","injured":"ferito","pavement":"marciapiede","siren":"sirena","bandage":"benda","headteacher":"preside",
 "degree":"laurea","do a degree":"fare una laurea","do a course":"fare un corso","do research":"fare ricerca",
 "research":"ricerca","qualification":"qualifica, titolo","get a qualification":"ottenere una qualifica",
 "pass an exam":"superare un esame","passed the exam":"ha superato l'esame","fail an exam":"essere bocciato a un esame",
 "failed the exam":"è stato bocciato all'esame","get good marks":"prendere bei voti","marks":"voti",
 "graduate":"laurearsi","gap year":"anno sabbatico","take a gap year":"prendersi un anno sabbatico",
 "revised":"ha ripassato","apply for a job":"candidarsi per un lavoro","interview":"colloquio",
 "have an interview":"fare un colloquio","had an interview":"ha fatto un colloquio","employee":"dipendente",
 "employer":"datore di lavoro","work for a company":"lavorare per un'azienda","work in a team":"lavorare in squadra",
 "salary":"stipendio","earn a good salary":"guadagnare un buono stipendio","make money":"guadagnare, fare soldi",
 "career":"carriera","have a career":"fare carriera","unemployed":"disoccupato","retire":"andare in pensione",
 "advert":"annuncio","solar panels":"pannelli solari","rents":"affitti","loan":"prestito",
 "make a decision":"prendere una decisione","make up my mind":"decidermi","make up her mind":"decidersi",
 "doubt":"dubbio","make a suggestion":"fare una proposta","suggestion":"proposta, suggerimento",
 "make an arrangement":"prendere accordi","arrangement":"accordo","make an appointment":"prendere un appuntamento",
 "appointment":"appuntamento","raise money":"raccogliere fondi",
 "make a mistake":"fare un errore","make an excuse":"trovare una scusa","excuse":"scusa, pretesto",
 "make an effort":"impegnarsi, sforzarsi","effort":"sforzo, impegno","make progress":"fare progressi",
 "progress":"progressi","make a noise":"fare rumore","make friends":"farsi degli amici","trust":"fiducia","tune":"melodia",
 "share a flat":"condividere un appartamento","stay single":"restare single","take up a new hobby":"iniziare un nuovo hobby",
 "do the cleaning":"fare le pulizie","do the washing":"fare il bucato","do housework":"fare i lavori di casa",
 "housework":"lavori di casa","do my hair":"sistemarmi i capelli","do her hair":"sistemarsi i capelli",
 "ironing":"stirare","irons":"stira","dusting":"spolverare","dust":"polvere, spolverare","dirt":"sporco","plait":"treccia",
 "curls":"ricci","curling iron":"arricciacapelli","pins":"forcine","knit":"lavorare a maglia","knitting":"lavorare a maglia",
 "vacuum":"passare l'aspirapolvere","scrubs":"strofina","flatmate":"coinquilino","nap":"pisolino","robotics":"robotica",
 "bills":"bollette","hang them out":"stenderli","coach":"allenatore","victims":"vittime","revision":"ripasso","anatomy":"anatomia","architecture firm":"studio di architettura","agency":"agenzia",
}

# Schede di studio: [voce, definizione, esempio nuovo, italiano] (+ True per i chunk da coprire interi)
STUDY = {
"1": [
 ["beautician", "a person whose job is to give treatments to the face, skin and nails, for example in a salon", "The beautician at the spa recommended a cream for my dry skin.", "estetista"],
 ["app developer", "a person who designs and writes the programs that people download on their phones", "Our school hired an app developer to create a timetable for students' phones.", "sviluppatore di app"],
 ["accountant", "a person whose job is to keep and check the financial records of a company or a person, and to prepare tax documents", "My uncle is an accountant, so in April his phone never stops ringing.", "commercialista, contabile"],
 ["lawyer", "a person who gives legal advice and represents people in court", "You should talk to a lawyer before you sign that contract.", "avvocato"],
 ["plumber", "a person who fits and repairs water pipes, taps, toilets and boilers", "The plumber says the old pipes under the sink need changing.", "idraulico"],
 ["personal trainer", "a fitness expert who plans exercises for one client at a time and checks their progress", "A personal trainer can be expensive, but she knows exactly what your body needs.", "personal trainer, allenatore personale"],
 ["journalist", "a person who collects news and writes articles or reports for newspapers, TV or websites", "A journalist from a national channel is visiting our town to film the flood damage.", "giornalista"],
 ["paramedic", "a person trained to give emergency help to sick or injured people, usually in an ambulance", "Paramedics work long night shifts and see terrible things.", "paramedico, soccorritore"],
],
"2": [
 ["do a degree", "degree: a university course of three or more years, in a subject such as law or physics", "My sister is doing a degree in architecture in Venice.", "fare una laurea", True],
 ["do a course", "course: a series of lessons on one subject, for example in the evenings or online", "Grandma is doing a course in computer skills at the library.", "fare un corso", True],
 ["do research", "research: careful study of a subject to discover new facts", "Scientists in Trieste do research on plastic in the sea.", "fare ricerca", True],
 ["get a qualification", "qualification: an official certificate that shows you have the skills for a job", "Nurses must get a qualification before they can look after patients.", "ottenere una qualifica, un titolo", True],
 ["pass an exam", "exam: an important test of what you know", "To pass an exam in law, you need weeks of study.", "superare un esame", True],
 ["fail an exam", "exam: an important test of what you know", "It's not the end of the world if you fail an exam — you can try again.", "essere bocciato a un esame", True],
 ["get good marks", "marks: the numbers or letters a teacher gives to show how good your work is", "To get good marks in English, you need to read a lot.", "prendere bei voti", True],
 ["graduate", "to finish your university studies and receive your diploma", "My father graduated in chemistry in 1995.", "laurearsi"],
 ["take a gap year", "gap year: twelve months of travel or work between school and university", "Many British students take a gap year to work abroad.", "prendersi un anno sabbatico", True],
],
"3": [
 ["apply for a job", "to ask formally for a position at work, usually by sending a CV and a letter", "Summer is a good time to apply for a job in a shop, because they need extra staff.", "candidarsi per un lavoro", True],
 ["have an interview", "interview: a meeting where an employer asks you questions to decide if you are right for a job", "Before you have an interview, find out about the company.", "fare un colloquio", True],
 ["work for a company", "to be an employee of a business", "Thousands of people in this area work for a company that makes glasses.", "lavorare per un'azienda", True],
 ["work in a team", "to do your job together with a group of colleagues", "Engineers usually work in a team with designers.", "lavorare in squadra", True],
 ["earn a good salary", "salary: the money you receive for your job, usually once a month", "Doctors earn a good salary, but their hours are very long.", "guadagnare un buono stipendio", True],
 ["make money", "to get money, for example from a job or by selling things", "My neighbour makes money by repairing old bikes.", "guadagnare, fare soldi", True],
 ["have a career", "career: the series of jobs you do in one area over many years", "Not everyone who studies music can have a career in an orchestra.", "fare carriera", True],
 ["be unemployed", "unemployed: without a paid job, but wanting one", "Unemployed people can join this course for free.", "essere disoccupato"],
 ["retire", "to stop working because you have reached a certain age", "Most people in Italy retire at sixty-seven.", "andare in pensione"],
],
"4": [
 ["make a decision", "decision: a choice you make after thinking about it", "Don't make a decision when you're angry.", "prendere una decisione", True],
 ["make up my mind", "to decide, especially after a period of doubt", "I can never make up my mind in an ice-cream shop.", "decidermi", True],
 ["make a suggestion", "suggestion: an idea that you give for other people to think about", "May I make a suggestion about the class party?", "fare una proposta, dare un suggerimento", True],
 ["make an arrangement", "arrangement: a plan you agree on with another person", "We usually make an arrangement to meet at the station.", "prendere accordi, mettersi d'accordo", True],
 ["make an appointment", "appointment: a fixed time to see a doctor, a dentist or another professional", "You must make an appointment to see the school counsellor.", "prendere un appuntamento", True],
],
"5": [
 ["make a mistake", "mistake: something that is wrong, for example in a test", "Anyone can make a mistake — the important thing is to learn from it.", "fare un errore", True],
 ["make an excuse", "excuse: a reason, often not true, that you give to explain why you can't do something", "He always makes an excuse to leave early.", "trovare una scusa", True],
 ["make an effort", "effort: hard physical or mental work to do something", "If you make an effort, the coach will notice.", "impegnarsi, sforzarsi", True],
 ["make progress", "progress: improvement or movement towards a goal", "Leo makes progress in German thanks to his podcasts.", "fare progressi", True],
 ["make a noise", "noise: a sound, often loud or unwanted", "Old houses make a noise at night when the wood cools down.", "fare rumore", True],
 ["make friends", "to meet new people and start relationships of trust with them", "It's easy to make friends at a summer camp.", "farsi degli amici", True],
],
"6": [
 ["share a flat", "flat: an apartment", "Students in big cities often share a flat to save money.", "condividere un appartamento", True],
 ["stay single", "to not get married or have a partner", "Some people decide to stay single and they're perfectly happy.", "restare single", True],
 ["take up a new hobby", "to start an activity for fun that you didn't do before", "At seventy, Grandad decided to take up a new hobby: pottery.", "iniziare un nuovo hobby", True],
 ["do the cleaning", "to make the house tidy and free of dust and dirt", "My aunt does the cleaning with loud music on.", "fare le pulizie", True],
 ["do the washing", "to wash clothes, usually in a machine", "On sunny days I do the washing early so that it dries quickly.", "fare il bucato", True],
 ["do housework", "housework: jobs at home such as ironing, dusting and washing up", "Teenagers should do housework too, not only their parents.", "fare i lavori di casa", True],
 ["do my hair", "to wash, brush and style your own hair", "I usually do my hair in five minutes: a quick ponytail.", "sistemarmi i capelli", True],
],
}

# voci di base tolte nella revisione (coerenza con le altre unità: lawyer e journalist sono già note)
_BASE = {"lawyer", "journalist"}
for _L in LEVELS:
    _L["items"] = [it for it in _L["items"] if it[3].lower() not in _BASE]
for _k in STUDY:
    STUDY[_k] = [r for r in STUDY[_k] if r[0].lower() not in _BASE]
