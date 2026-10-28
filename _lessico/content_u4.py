# Contenuti del lessico, Unit 4 "Book club"
from lexlib import *
UNIT = 4
NAME = "Book club"
TOPICS = "describing books · kinds of fiction · non-fiction and the book world · parts of a story · definizioni e collocazioni"
META = "adjectives to describe books, kinds of books, people in publishing, parts of a story"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — ADJECTIVES: WHEN WE LIKE A BOOK",
 desc="aggettivi positivi per libri, film e persone", rule=RULE, items=[
 D("«pleasant and attractive in a way that makes people like you at once» → ___", "(c…)", "charming", ["charming","charismatic"]),
 D("«giving pleasure; fun to read, watch or do» → ___", "(e…)", "enjoyable", ["enjoyable","entertaining","engaging"]),
 D("«simple and clear, so that you can get through it quickly and without effort» → ___", "(e…-t…-r…)", "easy-to-read", ["easy-to-read","easy to read"]),
 D("«full of useful facts that teach you something» → ___", "(i…)", "informative", ["informative","instructive"]),
 D("«convincing enough for you to accept that it is true» → ___", "(b…)", "believable"),
 D("«showing people and situations exactly the way they are in everyday life» → ___", "(r…)", "realistic"),
 D("«extremely good; excellent (informal)» → ___", "(t…)", "terrific", ["terrific","tremendous"]),
 G("Dario, the con man in the story, is so ___ — warm smile, kind words, flowers for each lady in the village — that nobody suspects him.", "(c…)", "charming", ["charming","charismatic"]),
 G("The book isn't a masterpiece, but it was ___ enough to keep me company on a long train journey to Bari.", "(e…)", "enjoyable", ["enjoyable","entertaining","engaging"]),
 G("With short chapters and simple language, this detective story is ___ — perfect for students at B1 level.", "(e…-t…-r…)", "easy-to-read", ["easy-to-read","easy to read"]),
 G("The museum leaflet is a bit boring, but it's very ___: dates, maps and the history of each room.", "(i…)", "informative", ["informative","instructive"]),
 G("I didn't like the ending: a girl of nine solves a murder that the police couldn't solve in thirty years. It just isn't ___.", "(b…)", "believable"),
 G("The hospital scenes are very ___: the author worked as a nurse for twenty years, and she gets each detail right.", "(r…)", "realistic"),
 G("— How was the book festival? — It was ___: great speakers, sunshine and free coffee all weekend.", "(t…)", "terrific", ["terrific","tremendous"]),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — ADJECTIVES: BAD BOOKS AND DARK STORIES",
 desc="aggettivi negativi · personaggi malvagi · storie paurose e tristi", rule=RULE, items=[
 D("«not special in any way; neither very good nor very bad» → ___", "(a…)", "average"),
 D("«very bad or unpleasant» → ___", "(a…)", "awful", ["awful","appalling","atrocious","abysmal"]),
 D("«less good than you hoped or expected» → ___", "(d…)", "disappointing"),
 D("«happy to make people or animals suffer» → ___", "(c…)", "cruel", ["cruel","callous"]),
 D("«extremely bad and wicked, like the dark lord in a fantasy story» → ___", "(e…)", "evil"),
 D("«so frightening that it makes you shake with fear» → ___", "(t…)", "terrifying"),
 D("«very sad, often because someone dies or suffers» → ___", "(t…)", "tragic"),
 G("On a scale from one to ten I'd give it a five: a very ___ thriller, with nothing new in it.", "(a…)", "average"),
 G("The food at the book launch was ___: cold pasta, warm flat cola and stale crisps.", "(a…)", "awful", ["awful","appalling","atrocious","abysmal"]),
 G("I had waited two years for the sequel, so it was really ___ to find it so much weaker than the first book.", "(d…)", "disappointing"),
 G("In the fairy tale, the ___ king locks his own daughter in a tower and feeds her only bread and water.", "(c…)", "cruel", ["cruel","callous"]),
 G("In the fantasy series, an ___ sorcerer wants to cover the whole world in darkness.", "(e…)", "evil"),
 G("The scene in the cellar is so ___ that my little brother hid behind the sofa and refused to watch the rest of the film.", "(t…)", "terrifying"),
 G("The novel is beautiful, but it has a ___ ending: the young soldier dies one day before the end of the war, and his mother never finds out.", "(t…)", "tragic"),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — gli aggettivi per descrivere un libro",
 desc="i primi due livelli insieme · frasi e definizioni nuove", items=[
 D("«with lots of facts and details, so you learn a lot from it» → ___", "(i…)", "informative", ["informative","instructive"]),
 G("Children love this author because his books are ___: big print, short sentences and a picture on each page.", "(e…-t…-r…)", "easy-to-read", ["easy-to-read","easy to read"]),
 D("«attractive and pleasant, with a manner that wins people over» → ___", "(c…)", "charming", ["charming","charismatic"]),
 G("The witch in the story is truly ___: she turns children into stone and laughs about it.", "(e…)", "evil"),
 G("I couldn't find the plot ___: the hero survives a plane crash, a shark attack and a volcano in one week, without a scratch.", "(b…)", "believable"),
 D("«very sad, with a terrible loss or death» → ___", "(t…)", "tragic"),
 G("Dad found the film ___: he had expected much more, because he had loved the book.", "(d…)", "disappointing"),
 G("The chapter in the haunted house was so ___ that I read the rest of the book with all the lights on.", "(t…)", "terrifying"),
 D("«nothing special; just ordinary» → ___", "(a…)", "average"),
 G("The service at the café near the library was ___: we waited an hour and the tea was cold.", "(a…)", "awful", ["awful","appalling","atrocious","abysmal"]),
 G("Nobody was surprised when the ___ landlord threw the family out into the snow on Christmas Eve.", "(c…)", "cruel", ["cruel","callous"]),
 D("«amusing and pleasant; something you like doing» → ___", "(e…)", "enjoyable", ["enjoyable","entertaining","engaging"]),
 G("Our trip to the children's book fair in Bologna was ___ — the best day of the school year!", "(t…)", "terrific", ["terrific","tremendous"]),
 G("The dialogue in the series is so ___ that you feel you're on the bus with a group of noisy teenagers.", "(r…)", "realistic"),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — KINDS OF FICTION",
 desc="gialli, fantasy, romanzi storici e rosa, fantascienza, racconti", rule=RULE, items=[
 D("«a long story told in pictures and speech bubbles, often for adult readers» → ___", "(g… n…)", "graphic novel"),
 D("«a long story about a murder or a robbery and the detective who finds out who did it» → ___", "(c… n…)", "crime novel"),
 D("«a long story set in an imaginary world with magic, dragons and wizards» → ___", "(f… n…)", "fantasy novel"),
 D("«a long story that takes place in the past, often with real events and people from those years» → ___", "(h… n…)", "historical novel"),
 D("«a long story about two people who fall in love» → ___", "(r… n…)", "romantic novel", ["romantic novel","romance novel"]),
 D("«stories about the future, space travel, robots and new technology» → ___", "(s… f…)", "science fiction", ["science fiction","sci-fi"]),
 D("«a piece of fiction that you can read in one sitting, much shorter than a novel» → ___", "(s… s…)", "short story"),
 D("«a book or film with an exciting plot, full of danger and suspense» → ___", "(t…)", "thriller"),
 G("My cousin draws comics for a living; her first ___ has two hundred pages of drawings and very little text.", "(g… n…)", "graphic novel"),
 G("In her new ___, Inspector Rossi has to find out who poisoned a rich old lady in a villa near Lake Como.", "(c… n…)", "crime novel"),
 G("The ___ that Tobia is reading has elves, a talking dragon and a map of an imaginary kingdom on the first page.", "(f… n…)", "fantasy novel"),
 G("Agnese loves ___: her favourite one takes place in Venice in 1630, during the plague.", "(h… n…)", "historical novels"),
 G("My aunt reads a ___ each week: there's always a misunderstanding, a wedding and a kiss in the final chapter.", "(r… n…)", "romantic novel", ["romantic novel","romance novel"]),
 G("Teo is crazy about ___: spaceships, time travel and robots that think like humans.", "(s… f…)", "science fiction", ["science fiction","sci-fi"]),
 G("The collection contains twelve ___, each one about twenty pages long.", "(s… s…)", "short stories"),
 G("I couldn't stop reading that ___: a spy, a stolen code and a chase across three countries in forty-eight hours.", "(t…)", "thriller"),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — NON-FICTION AND THE BOOK WORLD",
 desc="biografie, ricettari, libri di viaggio · chi scrive e chi pubblica · successi e recensioni", rule=RULE, items=[
 D("«the story of a person's life, written by that same person» → ___", "(a…)", "autobiography"),
 D("«a book about the life of a real person, by a different writer» → ___", "(b…)", "biography"),
 D("«a book full of recipes» → ___", "(c…)", "cookbook", ["cookbook","cook book","cookery book"]),
 D("«a book about a journey or a country, with descriptions of places and people» → ___", "(t… b…)", "travel book"),
 D("«a writer of long works of fiction» → ___", "(n…)", "novelist"),
 D("«a company that prepares books for sale and sends them to the shops» → ___", "(p…)", "publisher"),
 D("«a very popular book that many thousands of people buy» → ___", "(b…)", "bestseller", ["bestseller","best-seller","best seller"]),
 D("«a book so exciting that you can't stop reading it» → ___", "(p…-t…)", "page-turner", ["page-turner","page turner","pageturner"]),
 D("«an article that gives an opinion about a new book, film or show» → ___", "(r…)", "review"),
 G("The famous chef wrote her ___ at eighty: it tells her own life, from her childhood in a fishing village to her first restaurant in Paris.", "(a…)", "autobiography"),
 G("Yuki spent five years on the ___ of a forgotten woman inventor: she read her letters and interviewed her grandchildren.", "(b…)", "biography"),
 G("Mum's favourite ___ has ninety recipes for soups and a whole chapter on bread.", "(c…)", "cookbook", ["cookbook","cook book","cookery book"]),
 G("Before our trip to Scotland I bought a ___ about the Highlands, full of stories about castles, lochs and lonely islands.", "(t… b…)", "travel book"),
 G("Before she became a famous ___, Marta worked in a bank and wrote her first three books at night.", "(n…)", "novelist"),
 G("Elena sent her manuscript to forty ___ before one of them finally agreed to print it.", "(p…)", "publishers"),
 G("Silvio's first thriller sold only fifty copies in May, but after a famous actor praised it on TV, it ___ in a few weeks.", "(verbo + a b…)", "became a bestseller", ["became a bestseller","became a best-seller","became a best seller","turned into a bestseller"]),
 G("I started the book at ten in the evening and finished it at four in the morning — a real ___!", "(p…-t…)", "page-turner", ["page-turner","page turner","pageturner"]),
 G("After the school trip to the theatre, our teacher wants each of us to ___ of the play for the school magazine.", "(verbo + a r…)", "write a review"),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — PARTS OF A STORY",
 desc="capitoli, personaggi, trama, finale · eroine e cattivi · dove è ambientata", rule=RULE, items=[
 D("«one of the main sections of a book, usually with a number or a title» → ___", "(c…)", "chapter"),
 D("«a person in a novel, play or film» → ___", "(c…)", "character"),
 D("«the way a story finishes» → ___", "(e…)", "ending"),
 D("«the main female character of a story, usually brave and admired» → ___", "(h…)", "heroine"),
 D("«a picture or drawing in a book» → ___", "(i…)", "illustration", ["illustration","image"]),
 D("«the series of events that form the story of a novel or film» → ___", "(p…)", "plot"),
 D("«(of a story) taking place in a particular period or location» → ___", "(s… i…)", "set in"),
 D("«the main idea or message that a writer explores in a book» → ___", "(t…)", "theme"),
 D("«the bad character in a story who fights against the hero» → ___", "(v…)", "villain"),
 D("«a group of three books that tell one long story» → ___", "(t…)", "trilogy"),
 G("I'm only on ___ three, so please don't tell me who the murderer is!", "(c…)", "chapter"),
 G("My favourite ___ in the novel is the grumpy old fisherman who talks to his cat.", "(c…)", "character"),
 G("The film has a happy ___: the two brothers meet again after thirty years and open a restaurant together.", "(e…)", "ending"),
 G("The ___ of the novel is Aisha, a fearless young doctor who crosses the desert to save a village.", "(h…)", "heroine"),
 G("The ___ in my old copy of the book are beautiful: tiny pencil drawings of foxes and owls.", "(i…)", "illustrations", ["illustrations","images"]),
 G("I can't explain the ___ in two minutes: there are three families, two murders and a secret will.", "(p…)", "plot"),
 G("The novel is ___ a fishing village in Sicily in 1955, just after the war, and the sea is almost one of the characters.", "(s… i…)", "set in"),
 G("Friendship is the main ___ of the book: the author comes back to it in each chapter.", "(t…)", "theme", ["theme","topic"]),
 G("The ___ of the story is a smiling businessman who steals money from his own workers.", "(v…)", "villain"),
 G("The first book of the ___ is quite slow, but parts two and three are brilliant.", "(t…)", "trilogy"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — generi, mondo dei libri, parti della storia",
 desc="livelli 3-5 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«a book of drawings and speech bubbles, longer and more serious than a comic» → ___", "(g… n…)", "graphic novel"),
 G("The hero has to save the planet from an alien invasion in the year 3000 — classic ___.", "(s… f…)", "science fiction", ["science fiction","sci-fi"]),
 G("Mattia read the ___ of the singer and discovered that she had grown up in a tiny village near Trento.", "(b…)", "biography"),
 D("«a book that teaches you how to prepare dishes» → ___", "(c…)", "cookbook", ["cookbook","cook book","cookery book"]),
 G("The ___ of the play is Lady Morwen, a widow with a sweet smile and a bottle of poison in her bag.", "(v…)", "villain"),
 G("Our book club picked a ___ for March: a killer on a train, two detectives and a twist on the final page.", "(t…)", "thriller"),
 D("«the story of somebody's life told by the person who lived it» → ___", "(a…)", "autobiography"),
 G("The ___ in the new fantasy series is Mira, a girl of sixteen who rides a wolf into battle.", "(h…)", "heroine"),
 G("Davide waited two years for the third book of the ___, then read it in a weekend.", "(t…)", "trilogy"),
 D("«what happens in a story, from the start to the finish» → ___", "(p…)", "plot"),
 G("The influencer's ___ of the new restaurant gave it only one star, and half the tables stayed empty for a month.", "(r…)", "review"),
 G("The detective series is ___ Edinburgh, in dark, rainy streets below the castle.", "(s… i…)", "set in"),
 G("Nina reads one ___ of her novel on the bus to school and another on the way home.", "(c…)", "chapter"),
 D("«someone whose job is to write stories hundreds of pages long» → ___", "(n…)", "novelist"),
 G("I always read the ___ first: if it's sad, I don't buy the book.", "(e…)", "ending"),
 G("Lena's new mystery is a real ___: I took it to the beach and didn't look at the sea once.", "(p…-t…)", "page-turner", ["page-turner","page turner","pageturner"]),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Book club",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 G("Come on — a dog that drives a bus? The story is funny, but it's not exactly ___.", "(b…)", "believable"),
 D("«the wicked one in a story, the person readers love to hate» → ___", "(v…)", "villain"),
 G("We bought a ___ about Iceland before the trip: one chapter on volcanoes, one on hot springs, one on the people.", "(t… b…)", "travel book"),
 G("Leo's first novel ___ in six weeks; now his publisher wants two more books.", "(verbo + a b…)", "became a bestseller", ["became a bestseller","became a best-seller","became a best seller","turned into a bestseller"]),
 D("«causing great fear» → ___", "(t…)", "terrifying"),
 G("In his ___, the old mountain guide describes his own childhood on a farm in the Dolomites.", "(a…)", "autobiography"),
 D("«a long story with swords, magic and invented worlds» → ___", "(f… n…)", "fantasy novel"),
 G("The talk on bees was dry and slow, but highly ___: I came home with three pages of notes.", "(i…)", "informative", ["informative","instructive"]),
 G("Which ___ do you like best — the old farmer, the doctor or the little girl with the red bike?", "(c…)", "character"),
 G("It's a beautiful but ___ love story: the young couple drown in a storm on the day before their wedding.", "(t…)", "tragic"),
 D("«a printed criticism of a new film, book or concert» → ___", "(r…)", "review"),
 G("The chef's new ___ has photos of each dish and tips for beginners.", "(c…)", "cookbook", ["cookbook","cook book","cookery book"]),
 G("Simona's ___ follows three generations of one family: one book for the grandmother, one for the mother and one for the daughter.", "(t…)", "trilogy"),
 G("Gaia hated the stepsister in the fairy tale: she was ___ to the little cat and laughed when it cried.", "(c…)", "cruel", ["cruel","callous"]),
 G("The children's edition of the novel is ___ even for ten-year-olds: big letters, short sentences and a glossary at the back.", "(e…-t…-r…)", "easy-to-read", ["easy-to-read","easy to read"]),
 G("The ___ of Book Two, a gentle librarian who hides her secret past, has many fans among teenage readers.", "(h…)", "heroine"),
 G("I won't tell you the whole ___ — just that it starts with a missing cat and ends at a wedding.", "(p…)", "plot"),
 G("The new reading app is ___: it's light and fast, and the night mode is great.", "(t…)", "terrific", ["terrific","tremendous"]),
 G("That museum guide was ___: three pages on one teaspoon and nothing on the paintings.", "(a…)", "awful", ["awful","appalling","atrocious","abysmal"]),
 G("After all the promises in the trailer, the final episode was so ___ that thousands of fans asked for their money back.", "(d…)", "disappointing"),
]))

# glossa: parole difficili delle definizioni e delle frasi + significato delle risposte
GLOSS = {
 # risposte
 "charming":"affascinante, simpatico","charismatic":"carismatico","enjoyable":"piacevole","entertaining":"divertente, piacevole",
 "easy-to-read":"facile da leggere","informative":"informativo, istruttivo","instructive":"istruttivo","believable":"credibile",
 "realistic":"realistico","terrific":"fantastico, eccezionale","tremendous":"straordinario","average":"nella media, mediocre",
 "awful":"orribile, pessimo","appalling":"spaventoso, pessimo","atrocious":"atroce, pessimo","disappointing":"deludente",
 "cruel":"crudele","callous":"insensibile, spietato","evil":"malvagio","trailer":"trailer, anteprima","terrifying":"terrificante","tragic":"tragico",
 "graphic novel":"romanzo a fumetti","crime novel":"romanzo giallo","fantasy novel":"romanzo fantasy",
 "historical novel":"romanzo storico","historical novels":"romanzi storici","romantic novel":"romanzo rosa, romanzo d'amore",
 "romance novel":"romanzo rosa","science fiction":"fantascienza","sci-fi":"fantascienza","short story":"racconto",
 "short stories":"racconti","thriller":"thriller, romanzo di suspense","autobiography":"autobiografia","biography":"biografia",
 "cookbook":"libro di cucina, ricettario","travel book":"libro di viaggi","novelist":"romanziere, scrittore",
 "publisher":"casa editrice, editore","publishers":"case editrici, editori","bestseller":"bestseller, libro di grande successo",
 "became a bestseller":"è diventato un bestseller","become a bestseller":"diventare un bestseller",
 "page-turner":"libro che non si riesce a posare","review":"recensione","write a review":"scrivere una recensione",
 "chapter":"capitolo","character":"personaggio","characters":"personaggi","ending":"finale","heroine":"eroina, protagonista",
 "illustration":"illustrazione","illustrations":"illustrazioni","plot":"trama","set in":"ambientato in","theme":"tema",
 "topic":"argomento","villain":"cattivo, antagonista","trilogy":"trilogia",
 # parole difficili
 "convincing":"convincente","effort":"sforzo","wicked":"malvagio, perfido","suffer":"soffrire","shake":"tremare",
 "con man":"truffatore","compliments":"complimenti","suspects":"sospetta","masterpiece":"capolavoro","leaflet":"opuscolo",
 "speakers":"relatori","launch":"presentazione (di un libro)","stale":"stantio, vecchio","crisps":"patatine",
 "sequel":"seguito","fairy tale":"fiaba","tower":"torre","sorcerer":"stregone","cellar":"cantina","witch":"strega",
 "shark":"squalo","scratch":"graffio","haunted":"infestato dai fantasmi","landlord":"padrone di casa",
 "manner":"modo di fare","wins people over":"conquista le persone","speech bubbles":"nuvolette (dei fumetti)",
 "robbery":"rapina","wizards":"maghi","in one sitting":"tutto d'un fiato","suspense":"suspense, tensione",
 "poisoned":"avvelenato","elves":"elfi","kingdom":"regno","plague":"peste","misunderstanding":"malinteso",
 "spy":"spia","chase":"inseguimento","recipes":"ricette","lochs":"laghi scozzesi","manuscript":"manoscritto",
 "praised":"ha elogiato","debut":"primo libro, esordio","engaging":"coinvolgente","abysmal":"pessimo","admired":"ammirato","grumpy":"brontolone","fearless":"coraggioso, senza paura",
 "secret will":"testamento segreto","foxes":"volpi","owls":"gufi","widow":"vedova","poison":"veleno","twist":"colpo di scena",
 "wolf":"lupo","influencer":"influencer","mystery":"giallo, romanzo di mistero","criticism":"critica",
 "hot springs":"sorgenti termali","drown":"annegano","stepsister":"sorellastra","glossary":"glossario",
 "edition":"edizione","librarian":"bibliotecario/a","teaspoon":"cucchiaino","episode":"puntata","bees":"api",
 "dry":"arido, noioso","highly":"molto","inventor":"inventrice, inventore","dialogue":"dialoghi",
}

# Schede di studio: [voce, definizione inglese, esempio nuovo, italiano] (+ True per i chunk da coprire interi)
STUDY = {
"1": [
 ["charming", "pleasant and attractive in a way that makes people like you at once", "The old bookseller is so charming that customers stay for hours.", "affascinante, simpatico"],
 ["enjoyable", "giving pleasure; fun to read, watch or do", "Our afternoon at the writers' workshop was really enjoyable.", "piacevole"],
 ["easy-to-read", "simple and clear, so that you can get through it quickly and without effort", "The teacher gave me an easy-to-read version of the novel.", "facile da leggere"],
 ["informative", "full of useful facts that teach you something", "The documentary about volcanoes was short but informative.", "informativo, istruttivo"],
 ["believable", "convincing enough for you to accept that it is true", "The villain is believable because he has good reasons for his actions.", "credibile"],
 ["realistic", "showing people and situations exactly the way they are in everyday life", "The classroom scenes in that series are very realistic.", "realistico"],
 ["terrific", "extremely good; excellent (informal)", "We had a terrific time at the poetry night in the park.", "fantastico, eccezionale"],
],
"2": [
 ["average", "not special in any way; neither very good nor very bad", "For me it was just an average detective story.", "nella media, mediocre"],
 ["awful", "very bad or unpleasant", "The sound quality of the audiobook was awful.", "orribile, pessimo"],
 ["disappointing", "less good than you hoped or expected", "The film version of my favourite book was disappointing.", "deludente"],
 ["cruel", "happy to make people or animals suffer", "In the legend, the cruel giant keeps the villagers hungry.", "crudele"],
 ["evil", "extremely bad and wicked, like the dark lord in a fantasy story", "An evil queen poisons the river in the opening pages.", "malvagio"],
 ["terrifying", "so frightening that it makes you shake with fear", "That scream in the dark corridor is terrifying.", "terrificante"],
 ["tragic", "very sad, often because someone dies or suffers", "The novel tells the tragic tale of two brothers in the war.", "tragico"],
],
"3": [
 ["graphic novel", "a long story told in pictures and speech bubbles, often for adult readers", "We studied a graphic novel about the First World War in history.", "romanzo a fumetti, graphic novel"],
 ["crime novel", "a long story about a murder or a robbery and the detective who finds out who did it", "Grandma takes a crime novel to the beach each summer.", "romanzo giallo"],
 ["fantasy novel", "a long story set in an imaginary world with magic, dragons and wizards", "His first fantasy novel has a map of three kingdoms inside the cover.", "romanzo fantasy"],
 ["historical novel", "a long story that takes place in the past, often with real events and people from those years", "This historical novel takes place in Ravenna around the year 500.", "romanzo storico"],
 ["romantic novel", "a long story about two people who fall in love", "She hides the romantic novel inside her chemistry book.", "romanzo rosa, romanzo d'amore"],
 ["science fiction", "stories about the future, space travel, robots and new technology", "Science fiction often imagines life on other planets.", "fantascienza"],
 ["short story", "a piece of fiction that you can read in one sitting, much shorter than a novel", "He entered a short story in the school competition and won.", "racconto"],
 ["thriller", "a book or film with an exciting plot, full of danger and suspense", "That thriller kept me awake until two.", "thriller, romanzo di suspense"],
],
"4": [
 ["autobiography", "the story of a person's life, written by that same person", "Her autobiography opens with her first day at school.", "autobiografia"],
 ["biography", "the story of someone's life, written by another person", "I'm reading a biography of a famous mountain climber.", "biografia"],
 ["cookbook", "a book full of recipes", "Nonna's old cookbook is full of notes in pencil.", "libro di cucina, ricettario"],
 ["travel book", "a book about a journey or a country, with descriptions of places and people", "This travel book made me want to visit Portugal.", "libro di viaggi"],
 ["novelist", "a writer of long works of fiction", "The novelist signed copies after her talk at the library.", "romanziere, scrittore"],
 ["publisher", "a company that prepares books for sale and sends them to the shops", "A small publisher in Turin accepted his first manuscript.", "casa editrice, editore"],
 ["become a bestseller", "bestseller: a very popular book that many thousands of people buy", "Her debut could become a bestseller by Christmas.", "diventare un bestseller", True],
 ["page-turner", "a book so exciting that you can't stop reading it", "Take this page-turner on holiday, but don't start it at bedtime!", "libro che non si riesce a posare"],
 ["write a review", "review: an article that gives an opinion about a new book, film or show", "Nico writes a review on his blog for each book he finishes.", "scrivere una recensione", True],
],
"5": [
 ["chapter", "one of the main sections of a book, usually with a number or a title", "The first chapter is a bit slow, but then things get exciting.", "capitolo"],
 ["character", "a person in a novel, play or film", "The grandmother is the funniest character in the book.", "personaggio"],
 ["ending", "the way a story finishes", "Don't tell me the ending — I'm still reading it!", "finale"],
 ["heroine", "the main female character of a story, usually brave and admired", "In this book a young pilot from the 1930s is the heroine.", "eroina, protagonista"],
 ["illustration", "a picture or drawing in a book", "The illustrations in this children's book are by the author's son.", "illustrazione"],
 ["plot", "the series of events that form the story of a novel or film", "The plot is simple, but the dialogue is wonderful.", "trama"],
 ["set in", "(of a story) taking place in a particular period or location", "Most of her stories are set in small mountain villages.", "ambientato in"],
 ["theme", "the main idea or message that a writer explores in a book", "Loneliness is an important theme in his poems.", "tema"],
 ["villain", "the bad character in a story who fights against the hero", "In the cartoon the villain always wears a black hat.", "cattivo, antagonista"],
 ["trilogy", "a group of three books that tell one long story", "I've just bought the whole trilogy in one box.", "trilogia"],
],
}
