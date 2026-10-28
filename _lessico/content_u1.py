# Contenuti del lessico, Unit 1 "Use your time!"
from lexlib import *
CFG["split_pdg"] = True
UNIT = 1
SPLIT_PDG = True   # play/do/go si esercitano negli Esercitati: qui il verbo e' gia' nella frase
NAME = "Use your time!"
TOPICS = "hobbies and free time · sports and outdoor activities · dressing up · definizioni e collocazioni"
META = "hobbies, free time, sports and outdoor activities"
SK_VER = "v2"
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — MUSIC, GAMES AND PUZZLES",
 desc="band, batteria e cori · cruciverba, puzzle e scacchi", rule=RULE, items=[
 D("«a musical instrument with black and white keys that you press with your fingers» → ___", "(p…)", "piano"),
 D("«a set of instruments that you hit with sticks; the person who plays them sits at the back of the group» → ___", "(d…)", "drums"),
 D("«an instrument with six strings that you play with your fingers or with a small plastic pick» → ___", "(g…)", "guitar"),
 D("«a group of people who sing together, often at school or in a church» → ___", "(c…)", "choir"),
 D("«a small group of musicians who play pop or rock songs together» → ___", "(b…)", "band"),
 D("«a word game in a newspaper: you read the clues and write the answers in rows of little squares» → ___", "(c…)", "crossword", ["crossword","crosswords"]),
 D("«a game for two players on a board of black and white squares, with pieces such as the king, the queen and the knights» → ___", "(c…)", "chess"),
 D("«a picture cut into small pieces of different shapes that you put together again» → ___", "(p…)", "puzzle", ["puzzle","puzzles"]),
 D("«games that you play on a screen, with a controller or a keyboard» → ___", "(v… g…)", "video games", ["video games","videogames","video game"]),
 D("«a pack of fifty-two pieces of stiff paper with numbers and pictures, used for games such as poker» → ___", "(c…)", "cards"),
 G("Matteo writes his own songs, and now he wants to ___. He needs a drummer and a bass player.", "(verbo + in a b…)", "play in a band"),
 G("Before he got the job at the bank, my uncle used to ___ in a rock group — he still keeps the sticks in a drawer.", "(verbo + the d…)", "play the drums", ["play the drums","play drums"]),
 G("Lucia taught herself to ___ by watching online lessons; now she knows about twenty chords.", "(verbo + the g…)", "play the guitar", ["play the guitar","play guitar"]),
 G("You need strong, quick fingers to ___ well — and hours of practice on the keys.", "(verbo + the p…)", "play the piano", ["play the piano","play piano"]),
 G("On Sundays my aunt goes to church to ___; there are forty voices in it.", "(verbo + in a c…)", "sing in a choir", ["sing in a choir","sing in the choir"]),
 G("On the bus I put my headphones on and ___ until my stop.", "(verbo + to m…)", "listen to music"),
 G("Dad buys the newspaper only to ___ — he never reads the news.", "(verbo + c…)", "do crosswords", ["do crosswords","do the crossword","do the crosswords","do a crossword","do crossword puzzles","do the crossword puzzle"]),
 G("On rainy afternoons we ___ on the kitchen table; the one we finished in March had a thousand pieces.", "(verbo + p…)", "do puzzles", ["do puzzles","do jigsaw puzzles","do jigsaws"]),
 G("After dinner my grandparents ___ with the neighbours, and the loser washes the cups.", "(verbo + c…)", "play cards"),
 G("Can you ___? I need someone who knows how the knight moves on the board.", "(verbo + c…)", "play chess"),
 G("Mum doesn't let my brother ___ on school nights, so on Fridays he spends hours with the controller.", "(verbo + v… g…)", "play video games", ["play video games","play videogames"]),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — ARTS, CRAFTS AND COLLECTING",
 desc="creare con le mani · disegnare e dipingere · fare collezione", rule=RULE, items=[
 D("«to put together machines with motors and sensors that can move and do jobs on their own» → ___", "(b… r…)", "build robots", ["build robots","make robots"]),
 D("«to produce sticks of wax with a piece of string in the middle, for a soft yellow light» → ___", "(m… c…)", "make candles"),
 D("«rings, necklaces, earrings and bracelets» → ___", "(j…)", "jewellery", ["jewellery","jewelry"]),
 D("«small copies of planes, ships or cars that you build from a kit and glue together» → ___", "(m…)", "models", ["models","model"]),
 D("«to keep the small paper squares from letters and parcels, sorted in albums» → ___", "(c… s…)", "collect stamps"),
 D("«the hard outer cases of small sea creatures, often found on the beach» → ___", "(s…)", "shells"),
 D("«small decorative animals or people made of glass» → ___", "(g… f…)", "glass figures", ["glass figures","glass figurines"]),
 D("«to make a picture of something with a pencil or a pen» → ___", "(d…)", "draw"),
 D("«to make a picture with colours and a brush» → ___", "(p…)", "paint"),
 D("«objects for children to play with, such as dolls, little cars and teddy bears» → ___", "(t…)", "toys"),
 G("At the school tech club we ___ that can follow a black line on the floor.", "(verbo + r…)", "build robots", ["build robots","make robots"]),
 G("Aunt Ines melts old wax in a pan to ___, and gives them as presents at Christmas.", "(verbo + c…)", "make candles"),
 G("Nadia buys tiny beads and silver wire to ___; she sells the earrings at a market stall.", "(verbo + j…)", "make jewellery", ["make jewellery","make jewelry"]),
 G("Grandad has a table in the loft where he likes to ___ of old sailing ships, with glue and tiny brushes.", "(verbo + m…)", "make models", ["make models","build models"]),
 G("My great-uncle used to ___ from every country he visited; his albums are full of queens and presidents.", "(verbo + s…)", "collect stamps"),
 G("Each summer the twins ___ on the beach and keep them in glass jars on the windowsill.", "(verbo + s…)", "collect shells", ["collect shells","pick up shells","gather shells"]),
 G("Bruno has three shelves of tiny animals from Murano: he started to ___ in his twenties.", "(verbo + g… f…)", "collect glass figures", ["collect glass figures","collect glass figurines"]),
 G("Some adults ___ from the 1980s — an old action figure still in its box can be worth a lot of money.", "(verbo + t…)", "collect toys"),
 G("Sara takes a pencil everywhere and likes to ___ the people sitting opposite her on the train.", "(d…)", "draw", ins=I_WORD),
 G("In the art room the children wear old shirts to ___, because the colours stain everything.", "(p…)", "paint", ins=I_WORD),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — OTHER FREE-TIME ACTIVITIES",
 desc="cucina, ballo, volontariato · foto, teatro, video, blog · hobby e tempo libero", rule=RULE, items=[
 D("«to cook bread, cakes or biscuits in an oven» → ___", "(b…)", "bake"),
 D("«unpaid work that you do to help other people, for example at an animal shelter» → ___", "(v… w…)", "voluntary work"),
 D("«the art or hobby of taking pictures with a camera» → ___", "(p…)", "photography"),
 D("«a building where actors perform plays on a stage» → ___", "(t…)", "theatre", ["theatre","theater"]),
 D("«a website where someone writes regular posts about their life or interests» → ___", "(b…)", "blog"),
 D("«an activity that you do for pleasure in your free time» → ___", "(h…)", "hobby"),
 D("«the hours when you are not working or studying» → ___", "(f… t…)", "free time"),
 D("«to move your body to the rhythm of music» → ___", "(d…)", "dance"),
 G("On Sunday mornings Callum gets up early to ___ fresh bread for the whole family.", "(b…)", "bake", ins=I_WORD),
 G("At the wedding party everybody got up to ___ the moment the band started.", "(d…)", "dance", ins=I_WORD),
 G("Two afternoons a week Elena helps at the animal shelter: she likes to ___ for the community.", "(verbo + v… w…)", "do voluntary work"),
 G("Mia always takes three novels to the beach: she can ___ a whole one in an afternoon under the umbrella.", "(r…)", "read", ins=I_WORD),
 G("Leo spends hours on his phone instead of studying: he likes to ___ of cats and funny accidents.", "(verbo + v…)", "watch videos"),
 G("Ruby wants to ___ about her travels, with a new post each week and lots of photos.", "(verbo + a b…)", "write a blog", ["write a blog","start a blog"]),
 G("Our drama group performs at the local ___ in May, and the tickets sold out in two days.", "(t…)", "theatre", ["theatre","theater"], ins=I_WORD),
 G("Sasha's favourite hobby is ___: she never goes anywhere without her camera.", "(p…)", "photography", ins=I_WORD),
 G("— What do you usually do in your ___? — I go out with friends or I read.", "(f… t…)", "free time", ins=I_WORD),
 G("Collecting old coins is an unusual ___, but Otis is crazy about it.", "(h…)", "hobby", ins=I_WORD),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — musica, giochi, creatività, tempo libero",
 desc="i primi tre livelli insieme · frasi e definizioni nuove", items=[
 D("«a puzzle with numbered clues and a grid of black and white boxes» → ___", "(c…)", "crossword", ["crossword","crosswords"]),
 G("Tommaso took lessons at summer camp and learnt to ___: now he strums three songs on his six strings.", "(verbo + the g…)", "play the guitar", ["play the guitar","play guitar"]),
 G("Our grandmother still ___ at the parish church; she has a strong, clear voice and knows all the hymns.", "(verbo + in a c…)", "sings in a choir", ["sings in a choir","sings in the choir"]),
 D("«a small object of wax that burns slowly and gives light» → ___", "(c…)", "candle", ["candle","candles"]),
 G("My brother cuts the corners off foreign envelopes because he wants to ___.", "(verbo + s…)", "collect stamps"),
 G("On wet afternoons at the cottage we ___ on the floor — big ones, with pictures of sky and sea.", "(verbo + p…)", "do puzzles", ["do puzzles","do jigsaw puzzles","do jigsaws"]),
 D("«a small copy of a car, plane or ship, often built from plastic pieces» → ___", "(m…)", "model", ["model","models"]),
 G("Jamal wants to ___ about street food, with photos and reviews of his favourite stalls in town.", "(verbo + a b…)", "write a blog", ["write a blog","start a blog"]),
 G("Twice a year our class goes to the ___ in town to see a play in English.", "(t…)", "theatre", ["theatre","theater"], ins=I_WORD),
 G("Lisa helps old people with their shopping on Saturdays; she started to ___ at sixteen.", "(verbo + v… w…)", "do voluntary work"),
 G("Before the party we ___ a big chocolate cake in Mum's oven, and two trays of biscuits.", "(b…)", "baked", ins=I_WORD),
 G("On the train Noemi puts her earphones in and ___ for the whole journey.", "(verbo + to m…)", "listens to music"),
 D("«a person's favourite activity outside work or school» → ___", "(h…)", "hobby"),
 G("My uncle's knights and bishops trapped my king in ten moves. I need to learn to ___ properly.", "(verbo + c…)", "play chess"),
 G("Felix stays up till late to ___ online with players from Japan.", "(verbo + v… g…)", "play video games", ["play video games","play videogames"]),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — SPORTS",
 desc="fencing · gymnastics · weights · yoga · table tennis", rule=RULE, items=[
 D("«a sport in which two people fight with long, thin swords, wearing white clothes and a mask» → ___", "(f…)", "fencing"),
 D("«a sport with exercises on the floor, on bars and on a beam, which needs strength and balance» → ___", "(g…)", "gymnastics"),
 D("«heavy metal objects that you lift at the gym to make your muscles stronger» → ___", "(w…)", "weights"),
 D("«an activity from India with slow positions and breathing exercises for body and mind» → ___", "(y…)", "yoga"),
 D("«a team game where you bounce the ball and score points by throwing it into a high basket» → ___", "(b…)", "basketball"),
 D("«a game for two or four players who hit a small, light ball across a low net on a table» → ___", "(t… t…)", "table tennis"),
 D("«a team sport in which players hit a ball over a high net with their hands» → ___", "(v…)", "volleyball"),
 D("«a team sport with eleven players on each side who kick a ball and try to score goals» → ___", "(f…)", "football", ["football","soccer"]),
 G("You need fast reflexes and a good mask to ___ at competition level.", "(verbo + f…)", "do fencing", ["do fencing","practise fencing","practice fencing"]),
 G("At the age of seven Viola started to ___, and now she can do a perfect cartwheel on the beam.", "(verbo + g…)", "do gymnastics", ["do gymnastics","practise gymnastics","practice gymnastics"]),
 G("Gabriel goes to the gym twice a week to ___ because he wants stronger arms.", "(verbo + w…)", "do weights", ["do weights","lift weights"]),
 G("My mum likes to ___ before breakfast: twenty minutes of slow stretching and deep breathing.", "(verbo + y…)", "do yoga", ["do yoga","practise yoga","practice yoga"]),
 G("The PE teacher wants Davide to ___ for the school team because he is very tall.", "(verbo + b…)", "play basketball"),
 G("There's a table with a net at the youth club, so we often ___ after school.", "(verbo + t… t…)", "play table tennis"),
 G("In summer we ___ on the sand, four against four, with a net between two poles.", "(verbo + v…)", "play volleyball", ["play volleyball","play beach volleyball"]),
 G("My cousins ___ in the park on Saturdays and use two jackets as goalposts.", "(verbo + f…)", "play football", ["play football","play soccer"]),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — OUTDOOR ACTIVITIES",
 desc="acqua, neve, montagna, strada", rule=RULE, items=[
 D("«travelling on a river or a lake in a narrow boat that you move with a paddle» → ___", "(c…)", "canoeing"),
 D("«going up rocks or walls with your hands and feet, often with a rope and a helmet» → ___", "(c…)", "climbing"),
 D("«trying to catch fish with a rod and a line» → ___", "(f…)", "fishing"),
 D("«moving across ice on special boots with metal blades» → ___", "(i…)", "ice-skating", ["ice-skating","ice skating"]),
 D("«a water sport: you stand on a small board and a big kite pulls you across the waves» → ___", "(k…)", "kitesurfing", ["kitesurfing","kite surfing","kite-surfing"]),
 D("«riding a strong bike with thick tyres on hills and rough paths» → ___", "(m… b…)", "mountain biking"),
 D("«moving along on boots with a single line of small wheels» → ___", "(r…)", "rollerblading"),
 D("«travelling on water in a boat that the wind pushes» → ___", "(s…)", "sailing"),
 D("«coming down a snowy mountain standing on one wide board» → ___", "(s…)", "snowboarding"),
 D("«a long walk in the countryside or in the mountains, usually on paths» → ___", "(h…)", "hiking"),
 D("«moving through water using your arms and legs» → ___", "(s…)", "swimming"),
 D("«moving on foot at high speed, for exercise or in a race» → ___", "(r…)", "running"),
 G("Let's ___ on the river tomorrow: we can hire a boat and two paddles at the bridge.", "(verbo + c…)", "go canoeing", ["go canoeing","go kayaking"]),
 G("Bring a helmet and good shoes if you want to ___ on the rocks with us.", "(verbo + c…)", "go climbing", ["go climbing","go rock climbing"]),
 G("Grandpa wakes up at five to ___ at the lake, and he often comes home with nothing.", "(verbo + f…)", "go fishing"),
 G("In December the town puts an ice rink in the main square, so we can ___ after school.", "(verbo + i…)", "go ice-skating", ["go ice-skating","go ice skating","go skating"]),
 G("Tarifa is the perfect place to ___: there's strong wind almost all year.", "(verbo + k…)", "go kitesurfing", ["go kitesurfing","go kite surfing","go kite-surfing"]),
 G("On Sundays Dario and his friends ___ on the rough paths above the village.", "(verbo + m… b…)", "go mountain biking"),
 G("We used to ___ along the seafront, with knee pads and helmets.", "(verbo + r…)", "go rollerblading"),
 G("My dad puts on his trainers and ___ in the park before work.", "(verbo + r…)", "goes running", ["goes running","goes jogging"]),
 G("With the right wind, my uncle takes his small boat out of the harbour to ___.", "(verbo + s…)", "go sailing"),
 G("Elisa prefers to ___ instead of skiing: one board is enough for her.", "(verbo + s…)", "go snowboarding"),
 G("The pool opens at seven, so on Tuesdays I ___ before school.", "(verbo + s…)", "go swimming"),
 G("We packed sandwiches and water to ___ in the mountains for the whole day.", "(verbo + h…)", "go hiking", ["go hiking","go trekking"]),
 G("My parents like to ___ in the hills on Sunday afternoons — nothing fast, just a quiet stroll.", "(verbo + w…)", "go walking"),
]))

# ---------------------------------------------------------------- 06
LEVELS.append(dict(id=6, type="study", title="LIVELLO 06 — DRESSING UP AND LEARNING HOW",
 desc="cosplay, costumi, feste in maschera · chiedere come si fa", rule=RULE, items=[
 D("«a hobby in which fans dress like characters from comics, films or video games» → ___", "(c…)", "cosplay"),
 D("«the clothes you wear to look like a different person or character, for example in a show» → ___", "(c…)", "costume"),
 D("«a large event where fans of comics, games or films meet, buy things and show their outfits» → ___", "(c…)", "convention"),
 D("«an elegant party where all the guests wear masks, typical of Venice» → ___", "(m… b…)", "masquerade ball"),
 D("«clothes that make you look like a pirate, an animal or a famous person at a party» → ___", "(f… d…)", "fancy dress"),
 G("For the comics fair, Kevin wants to ___ a superhero, with a cape and a mask.", "(d… u… a…)", "dress up as", ins=I_WORD),
 G("Marta spent three months sewing her ___ for the fair: each detail is exactly as in the film.", "(c…)", "costume", ins=I_WORD),
 G("The invitation says the party is ___, so I need to look like a pirate or a vampire.", "(f… d…)", "fancy dress", ins=I_WORD),
 G("Thousands of fans travel to Lucca for the comics ___ at the end of October.", "(c…)", "convention", ins=I_WORD),
 G("In Venice, during Carnival, you can buy a ticket for a ___ in an old palace — masks are obligatory.", "(m… b…)", "masquerade ball", ins=I_WORD),
 G("Keira's hobby is ___: she makes her own outfits and goes to events dressed as her favourite anime characters.", "(c…)", "cosplay", ins=I_WORD),
 G("— ___ make a paper plane? — First, fold the sheet in half.", "(H… d… y…)", "How do you", ins="Completa la domanda."),
 G("— ___ tie this knot? I can't do it on my own. — Sure, watch me.", "(C… y… s… m… h… t…)", "Can you show me how to", ins="Completa la domanda."),
 G("— The wings are on the plane. ___? — Now paint the body.", "(W… d… I d… n…)", "What do I do next", ins="Completa la domanda."),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — sport, attività all'aperto, travestimenti",
 desc="livelli 4-6 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«a game for two teams of six, played by hitting a ball over a net with your hands» → ___", "(v…)", "volleyball"),
 G("Bianca ___ three times a week; her best event is the beam.", "(verbo + g…)", "does gymnastics", ["does gymnastics","practises gymnastics","practices gymnastics"]),
 D("«exercise in which you lift heavy bars and dumbbells» → ___", "(w…)", "weights", ["weights","weightlifting","weight lifting"]),
 G("The lake freezes in January, so the children put on warm coats and ___ after lunch.", "(verbo + i…)", "go ice-skating", ["go ice-skating","go ice skating","go skating"]),
 G("Before work, Rosa ___ along the river: five kilometres in thirty minutes.", "(verbo + r…)", "goes running", ["goes running","goes jogging"]),
 D("«a sport on snow: you slide down with both feet fixed to one board» → ___", "(s…)", "snowboarding"),
 G("My cousins hired a small boat at the harbour and ___ along the coast for three days.", "(verbo + s…)", "went sailing"),
 G("The masks were ready and the orchestra was playing: the ___ in the old palace started at nine.", "(m… b…)", "masquerade ball", ins=I_WORD),
 D("«a big meeting of fans with stands, special guests and costume competitions» → ___", "(c…)", "convention"),
 G("Pietro bought a cape and plastic teeth: he wants to ___ a vampire at the carnival party.", "(d… u… a…)", "dress up as", ins=I_WORD),
 G("— ___ change the strings on this guitar? — First loosen them, then pull them out.", "(H… d… y…)", "How do you", ins="Completa la domanda."),
 G("— The cards are on the table. ___? — Now give seven to each player.", "(W… d… I d… n…)", "What do I do next", ins="Completa la domanda."),
 G("In Lucca, Sami walked around all day in his handmade knight's ___.", "(c…)", "costume", ins=I_WORD),
 G("Our team needs one more player to ___ on Saturday: we're only ten.", "(verbo + f…)", "play football", ["play football","play soccer"]),
 D("«a sport in which you hit a light ball with a small bat across a table» → ___", "(t… t…)", "table tennis"),
 G("If you like wind and waves, try to ___ in Sardinia: the kite pulls you along the water.", "(verbo + k…)", "go kitesurfing", ["go kitesurfing","go kite surfing","go kite-surfing"]),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Use your time!",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 G("Alice keeps a paddle and a life jacket in the car to ___ on the lake after work.", "(verbo + c…)", "go canoeing", ["go canoeing","go kayaking"]),
 D("«a hobby: making pictures of landscapes or people with brushes and colours» → ___", "(p…)", "painting"),
 G("Arturo keeps the cars and dolls of his childhood in boxes: he likes to ___ from the seventies.", "(verbo + t…)", "collect toys"),
 G("My sister's club meets on Thursdays to ___ with small motors and sensors.", "(verbo + r…)", "build robots", ["build robots","make robots"]),
 G("Kai ___ on rough tracks in the hills; his bike has thick tyres and strong brakes.", "(verbo + m… b…)", "goes mountain biking"),
 G("In our village there's a club where you can ___ with real swords and masks.", "(verbo + f…)", "do fencing", ["do fencing","practise fencing","practice fencing"]),
 G("Halfway up the rock face, Ivan stopped for some water. He loves to ___ with ropes and a harness.", "(verbo + c…)", "go climbing", ["go climbing","go rock climbing"]),
 G("Chiara spends her Sunday mornings in the kitchen: she loves to ___ cakes for her friends.", "(b…)", "bake", ins=I_WORD),
 G("Ugo has a good voice, so he wants to ___ at school: there are forty singers and a concert in June.", "(verbo + in a c…)", "sing in a choir", ["sing in a choir","sing in the choir"]),
 G("Gaia took her camera to the mountains: ___ is her great passion.", "(p…)", "photography", ins=I_WORD),
 G("Dad and I ___ at dawn, but we didn't catch anything, not even a small one.", "(verbo + f…)", "went fishing"),
 D("«a sport for two teams of five who bounce a ball and throw it through a hoop» → ___", "(b…)", "basketball"),
 G("Before an exam I ___ to relax: slow positions and deep breaths.", "(verbo + y…)", "do yoga", ["do yoga","practise yoga","practice yoga"]),
 G("— ___ fold the shirt like that? It looks perfect. — Sure, watch.", "(C… y… s… m… h… t…)", "Can you show me how to", ins="Completa la domanda."),
 G("Asia threads coloured beads to ___; she started at fourteen and now sells bracelets online.", "(verbo + j…)", "make jewellery", ["make jewellery","make jewelry"]),
 G("Six of us stayed at the beach till dark and ___ with a ball and a net.", "(verbo + v…)", "played volleyball", ["played volleyball","played beach volleyball"]),
 G("Matilde puts on her wrist guards and ___ along the seafront, between the walkers and the bikes.", "(verbo + r…)", "goes rollerblading"),
 G("It rains all afternoon at the campsite, so we sit in the tent and ___.", "(verbo + c…)", "play cards"),
 G("Lorenzo sits at his desk for hours to ___ of famous ships, with glue and tweezers.", "(verbo + m…)", "make models", ["make models","build models"]),
 D("«a party where people wear clothes that make them look like someone or something else» → ___", "(f… d…)", "fancy dress"),
]))

# --- voci di base (livello primo anno): fuori dal file, decisione di Cristina 28/10 ---
BASIC = {"guitar","piano","cards","video games","music","draw","paint","painting","dance","read","videos",
         "hobby","free time","listen to music","listens to music","watch videos","football","basketball","volleyball","swimming","running","walking","bake","baked"}
for L in LEVELS:
    L["items"] = [it for it in L["items"] if it[3].lower() not in BASIC]
# il livello 3 resta piccolo: confluisce nel 2, e i livelli successivi scalano di uno
l2 = next(L for L in LEVELS if L["id"] == 2); l3 = next(L for L in LEVELS if L["id"] == 3)
l2["items"] += l3["items"]; LEVELS.remove(l3)
l2["title"] = "LIVELLO 02 — CRAFTS, COLLECTING AND MORE"
l2["desc"] = "creare con le mani · fare collezione · volontariato, foto, teatro, blog"
for L in LEVELS:
    if isinstance(L["id"], int) and L["id"] > 3:
        L["title"] = L["title"].replace("LIVELLO %02d" % L["id"], "LIVELLO %02d" % (L["id"] - 1)); L["id"] -= 1
LEVELS[[L["id"] for L in LEVELS].index("rA")]["title"] = "⟳ RIPASSO A — musica, giochi, creatività"
LEVELS[[L["id"] for L in LEVELS].index("rA")]["desc"] = "i primi due livelli insieme · frasi e definizioni nuove"
LEVELS[[L["id"] for L in LEVELS].index("rB")]["desc"] = "livelli 3-5 e qualcosa di prima · frasi e definizioni nuove"

# glossa: parole difficili delle definizioni e significato delle risposte (visibile al tocco
# nelle frasi e nella correzione, mai prima della risposta)
GLOSS = {
 "keys":"tasti","strings":"corde","pick":"plettro","sticks":"bacchette","choir":"coro","band":"gruppo musicale",
 "clues":"definizioni (cruciverba)","rows":"righe","crossword":"cruciverba","crosswords":"cruciverba","chess":"scacchi",
 "knights":"cavalli (scacchi)","knight":"cavallo (scacchi)","puzzle":"puzzle","puzzles":"puzzle","stiff":"rigido",
 "drums":"batteria","chords":"accordi","loser":"chi perde","controller":"controller",
 "wax":"cera","string":"stoppino","candles":"candele","candle":"candela","jewellery":"gioielli, bigiotteria",
 "beads":"perline","wire":"filo metallico","earrings":"orecchini","bracelets":"braccialetti","necklaces":"collane",
 "kit":"scatola di montaggio","glue":"colla","stamps":"francobolli","envelope":"busta","envelopes":"buste",
 "shells":"conchiglie","glass figures":"figurine di vetro","toys":"giocattoli","teddy bears":"orsacchiotti",
 "stain":"macchiare","jars":"barattoli","windowsill":"davanzale","loft":"soffitta","action figure":"personaggio giocattolo",
 "voluntary work":"volontariato","shelter":"rifugio, canile","photography":"fotografia","theatre":"teatro",
 "blog":"blog","hobby":"passatempo","free time":"tempo libero","stall":"bancarella","stalls":"bancarelle",
 "fencing":"scherma","swords":"spade","gymnastics":"ginnastica artistica","beam":"trave","cartwheel":"ruota",
 "weights":"pesi","dumbbells":"manubri","yoga":"yoga","table tennis":"ping pong","volleyball":"pallavolo",
 "goalposts":"pali della porta","bat":"racchetta","hoop":"canestro","reflexes":"riflessi",
 "canoeing":"canoa","paddle":"pagaia","paddles":"pagaie","climbing":"arrampicata","rope":"corda","ropes":"corde",
 "harness":"imbracatura","fishing":"pesca","rod":"canna da pesca","ice-skating":"pattinaggio sul ghiaccio",
 "blades":"lame","rink":"pista di pattinaggio","kitesurfing":"kitesurf","kite":"aquilone","mountain biking":"mountain bike",
 "tyres":"pneumatici","rollerblading":"pattinaggio in linea","inline skates":"pattini in linea","sailing":"vela",
 "snowboarding":"snowboard","hiking":"escursionismo","stroll":"passeggiata","harbour":"porto","seafront":"lungomare",
 "knee pads":"ginocchiere","cosplay":"cosplay","costume":"costume","convention":"fiera, raduno",
 "masquerade ball":"ballo in maschera","fancy dress":"travestimento, festa in maschera","dress up as":"travestirsi da",
 "cape":"mantello","outfits":"abiti, travestimenti","knot":"nodo","sewing":"cucire","threads":"infila",
 "tweezers":"pinzette","strums":"strimpella","hymns":"inni sacri","bishops":"alfieri","harness":"imbracatura",
 "dawn":"alba","tracks":"sentieri","grid":"griglia","sensors":"sensori",
}


# Schede di studio della Unit 1: [voce, definizione inglese, esempio nuovo, italiano]
# Le definizioni sono le stesse degli esercizi (lo studente le riconosce);
# gli esempi sono nuovi e non devono somigliare alle frasi degli esercizi o del libro.
STUDY = {
"1": [
 ["listen to music", "to pay attention to songs, for example through headphones", "I listen to music in my room, but only songs without words.", "ascoltare musica"],
 ["play in a band", "band: a small group of musicians who play pop or rock songs together", "My brother plays in a band with three friends from school.", "suonare in un gruppo"],
 ["play the drums", "drums: a set of instruments that you hit with sticks", "Leo plays the drums in the garage on Saturday mornings.", "suonare la batteria"],
 ["play the guitar", "guitar: an instrument with six strings that you play with your fingers or a pick", "She plays the guitar and sings at the same time.", "suonare la chitarra"],
 ["play the piano", "piano: an instrument with black and white keys", "My grandfather still plays the piano at family parties.", "suonare il pianoforte"],
 ["sing in a choir", "choir: a group of people who sing together, often at school or in a church", "My mother sings in a choir that performs at weddings.", "cantare in un coro"],
 ["do crosswords", "crossword: a word game with clues and rows of little squares", "My uncle does crosswords on the train to work.", "fare le parole crociate"],
 ["do puzzles", "puzzle: a picture cut into small pieces that you put together again", "At Christmas the whole family does puzzles in the living room.", "fare i puzzle"],
 ["play cards", "cards: a pack of fifty-two pieces of stiff paper used for games", "On holiday we play cards on the balcony after dinner.", "giocare a carte"],
 ["play chess", "chess: a game for two players on a board of black and white squares", "Ilaria plays chess online with people from all over the world.", "giocare a scacchi"],
 ["play video games", "video games: games that you play on a screen, with a controller or a keyboard", "Some of my friends play video games until two in the morning.", "giocare ai videogiochi"],
],
"2": [
 ["build robots", "robots: machines that can move and do jobs on their own", "In the robotics club we build robots for a national competition.", "costruire robot"],
 ["draw", "to make a picture of something with a pencil or a pen", "Can you draw a horse? Mine always look like dogs.", "disegnare"],
 ["make candles", "candles: sticks of wax with a piece of string in the middle that you light", "You can make candles at home with an old pan.", "fare candele"],
 ["make jewellery", "jewellery: rings, necklaces, earrings and bracelets", "My cousin makes jewellery with tiny pieces of coloured glass.", "creare gioielli, bigiotteria"],
 ["make models", "models: small copies of planes, ships or cars that you build from a kit", "He makes models of famous racing cars.", "costruire modellini"],
 ["paint", "to make a picture with colours and a brush", "On holiday Elena paints the fishing boats in the port.", "dipingere"],
 ["collect glass figures", "glass figures: small decorative animals or people made of glass", "My aunt collects glass figures, especially birds.", "collezionare figurine di vetro"],
 ["collect shells", "shells: the hard outer cases of small sea creatures", "My little sister collects shells and keeps them in a box.", "raccogliere conchiglie"],
 ["collect stamps", "stamps: small paper squares that you stick on an envelope", "Not many young people collect stamps today.", "collezionare francobolli"],
 ["collect toys", "toys: objects for children to play with, such as dolls and teddy bears", "Some people collect toys from old cartoons.", "collezionare giocattoli"],
],
"3": [
 ["bake", "to cook bread, cakes or biscuits in an oven", "Let's bake some biscuits for tomorrow's party.", "cuocere al forno, fare dolci"],
 ["dance", "to move your body to the rhythm of music", "At parties I never dance before midnight.", "ballare"],
 ["do voluntary work", "voluntary work: unpaid work that you do to help other people", "In July I do voluntary work at a summer camp for children.", "fare volontariato"],
 ["photography", "the art or hobby of taking pictures with a camera", "Dario became interested in photography on a school trip.", "fotografia"],
 ["read", "to look at written words and understand them", "I read on the bus, but it makes me feel sick.", "leggere"],
 ["theatre", "a building where actors perform plays on a stage", "The old theatre in our town has red velvet seats.", "teatro"],
 ["watch videos", "videos: short films that you watch online", "We watch videos about cooking and then try the recipes.", "guardare video"],
 ["write a blog", "blog: a website where someone writes regular posts about their life or interests", "Our English teacher writes a blog about books for teenagers.", "scrivere un blog"],
 ["hobby", "an activity that you do for pleasure in your free time", "Is gardening a hobby for old people? Not at all!", "passatempo, hobby"],
 ["free time", "the hours when you are not working or studying", "I don't have much free time during the week.", "tempo libero"],
],
"4": [
 ["do fencing", "fencing: a sport in which two people fight with long, thin swords", "Giada does fencing at a club in Verona.", "fare scherma"],
 ["do gymnastics", "gymnastics: a sport with exercises on the floor, on bars and on a beam", "My little sister does gymnastics on Tuesdays and Fridays.", "fare ginnastica artistica"],
 ["do weights", "weights: heavy metal objects that you lift at the gym", "He does weights at the gym to stay in shape.", "fare pesi"],
 ["do yoga", "yoga: an activity from India with slow positions and breathing exercises", "My dad does yoga to help his bad back.", "fare yoga"],
 ["play basketball", "basketball: a team game where you score points by throwing the ball into a high basket", "We play basketball in the school gym at lunchtime.", "giocare a basket"],
 ["play football", "football: a team sport with eleven players who kick a ball and score goals", "Do you play football or just watch it on TV?", "giocare a calcio"],
 ["play table tennis", "table tennis: a game in which players hit a small, light ball across a low net on a table", "In winter we play table tennis in my grandparents' cellar.", "giocare a ping pong"],
 ["play volleyball", "volleyball: a team sport in which players hit a ball over a high net with their hands", "Our class plays volleyball against the teachers each June.", "giocare a pallavolo"],
],
"5": [
 ["go canoeing", "canoeing: travelling on a river or a lake in a narrow boat that you move with a paddle", "We went canoeing on the Adige with our PE teacher.", "fare canoa"],
 ["go climbing", "climbing: going up rocks or walls with your hands and feet", "Never go climbing without a helmet.", "fare arrampicata"],
 ["go fishing", "fishing: trying to catch fish with a rod and a line", "My grandfather and I go fishing on Sunday mornings.", "andare a pesca"],
 ["go ice-skating", "ice-skating: moving across ice on special boots with metal blades", "We go ice-skating at the rink near the stadium.", "pattinare sul ghiaccio"],
 ["go kitesurfing", "kitesurfing: a water sport in which a big kite pulls you across the waves on a board", "You need strong wind to go kitesurfing.", "fare kitesurf"],
 ["go mountain biking", "mountain biking: riding a strong bike with thick tyres on hills and rough paths", "In summer my cousins go mountain biking near Lake Garda.", "andare in mountain bike"],
 ["go rollerblading", "rollerblading: moving along on boots with a single line of small wheels", "Wear knee pads when you go rollerblading.", "pattinare in linea"],
 ["go running", "running: moving on foot at high speed, for exercise or in a race", "I go running in the park three times a week.", "andare a correre"],
 ["go sailing", "sailing: travelling on water in a boat that the wind pushes", "In August we go sailing along the coast of Croatia.", "andare in barca a vela"],
 ["go snowboarding", "snowboarding: coming down a snowy mountain standing on one wide board", "My friends go snowboarding in the Dolomites in February.", "fare snowboard"],
 ["go swimming", "swimming: moving through water using your arms and legs", "Let's go swimming after school: the pool is open until eight.", "andare a nuotare"],
 ["go walking", "walking: moving on foot at a normal speed, for pleasure", "Older people often go walking together in the mornings.", "andare a camminare"],
 ["go hiking", "hiking: a long walk in the countryside or in the mountains, usually on paths", "Bring a map if you go hiking in an area you don't know.", "fare escursioni"],
],
"6": [
 ["cosplay", "a hobby in which fans dress like characters from comics, films or video games", "Cosplay is popular at comics fairs all over the world.", "cosplay"],
 ["costume", "the clothes you wear to look like a different person or character", "Her pirate costume won first prize.", "costume"],
 ["fancy dress", "clothes that make you look like a pirate, an animal or a famous person at a party", "We went to the end-of-year party in fancy dress.", "travestimento, festa in maschera"],
 ["convention", "a large event where fans of comics, games or films meet", "The convention attracts fans from many different countries.", "fiera, raduno"],
 ["masquerade ball", "an elegant party where all the guests wear masks", "A masquerade ball is a typical Carnival event in Venice.", "ballo in maschera"],
 ["dress up as", "to put on clothes to look like a character or a different person", "My little brother wants to dress up as a dinosaur.", "travestirsi da"],
 ["How do you…?", "a question to ask the way to do something", "How do you switch on this projector?", "Come si…?"],
 ["Can you show me how to…?", "a request to see how someone does something", "Can you show me how to make a video call?", "Mi fai vedere come si…?"],
 ["What do I do next?", "a question to ask for the following step", "The paper is cut. What do I do next?", "E adesso cosa faccio?"],
],
}

BASIC_ST = {"listen to music","play the guitar","play the piano","play cards","play video games","draw","paint","dance",
            "read","watch videos","hobby","free time","play football","play basketball","play volleyball",
            "go swimming","go running","go walking","bake"}
for k in list(STUDY): STUDY[k] = [r for r in STUDY[k] if r[0] not in BASIC_ST]
STUDY["2"] += STUDY.pop("3")
STUDY = {"1": STUDY["1"], "2": STUDY["2"], "3": STUDY["4"], "4": STUDY["5"], "5": STUDY["6"]}

CHUNK_HEADS = ("make ","build ","collect ","sing ","write ","dress ")
for _k in STUDY:
    STUDY[_k] = [r + [True] if r[0].startswith(CHUNK_HEADS) else r for r in STUDY[_k]]
