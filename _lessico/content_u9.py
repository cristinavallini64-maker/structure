# Contenuti del lessico, Unit 9 "Made to measure"
from lexlib import *
UNIT = 9
NAME = "Made to measure"
TOPICS = "fabrics and materials · shapes and patterns · size and appearance · inventions · definizioni e collocazioni"
META = "fabrics, materials, shapes, patterns, size and inventions"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — FABRICS",
 desc="seta, velluto, pizzo, jeans · pelle ed ecopelle · lana", rule=RULE, items=[
 D("«a soft, smooth, shiny cloth made from the threads that a small caterpillar produces» → ___", "(s…)", "silk"),
 D("«a small caterpillar that wraps itself in a cocoon of fine thread; people use this thread to make expensive cloth» → ___", "(s…)", "silkworm", ["silkworm","silkworms","silk worm"]),
 D("«a heavy cloth with a thick, very soft surface, used for cushions and elegant jackets» → ___", "(v…)", "velvet"),
 D("«a delicate cloth with a pattern of small holes, often used on wedding dresses and tablecloths» → ___", "(l…)", "lace"),
 D("«a strong cotton cloth, usually blue, used to make jeans» → ___", "(d…)", "denim"),
 D("«animal skin that is treated and used to make shoes, bags, belts and jackets» → ___", "(l…)", "leather"),
 D("«a material that looks like animal skin but is produced without harming any animals» → ___", "(e… l…)", "eco-friendly leather", ["eco-friendly leather","eco friendly leather","eco-leather","eco leather"]),
 D("«made of the soft, thick hair of sheep» → ___", "(w…)", "woollen", ["woollen","woolen","wool"]),
 G("The area around Lake Como is famous for its ___ industry: farmers once grew mulberry trees there to feed the caterpillars.", "(s…)", "silk"),
 G("A ___ eats nothing but leaves for a month, then spins its cocoon in about three days.", "(s…)", "silkworm", ["silkworm","silk worm"]),
 G("The old cinema had red ___ seats, soft to the touch like a cat's fur.", "(v…)", "velvet"),
 G("Aunt Rita's wedding veil is decorated with fine ___ from Burano, an island famous for it.", "(l…)", "lace"),
 G("My brother's work jacket is made of organic ___, and it gets softer each time he washes it.", "(d…)", "denim"),
 G("This bag is genuine ___ — the shop assistant showed me the stamp of the tannery inside.", "(l…)", "leather"),
 G("No animal was harmed for this jacket: it's ___, produced from apple peel.", "(e… l…)", "eco-friendly leather", ["eco-friendly leather","eco friendly leather","eco-leather","eco leather"]),
 G("Put on a thick ___ jumper: it's freezing on the boat.", "(w…)", "woollen", ["woollen","woolen","wool"]),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — METALS, STONES AND OTHER MATERIALS",
 desc="rame, platino, diamanti · mattoni, legno, paglia · materiali riciclati", rule=RULE, items=[
 D("«a reddish-brown metal that carries electricity well and turns green with time» → ___", "(c…)", "copper"),
 D("«a rare, heavy, silver-white precious metal, used for rings and in car parts» → ___", "(p…)", "platinum"),
 D("«a very hard, clear precious stone, often used in engagement rings» → ___", "(d…)", "diamond", ["diamond","diamonds"]),
 D("«a hard block of baked clay used to build walls and houses» → ___", "(b…)", "brick", ["brick","bricks"]),
 D("«made of the hard material that comes from trees» → ___", "(w…)", "wooden"),
 D("«dry yellow stems of wheat, used for summer hats, baskets and animal beds» → ___", "(s…)", "straw"),
 D("«made again from things that people threw away, such as old bottles or paper» → ___", "(r…)", "recycled"),
 G("Most electric cables have ___ wires inside because this metal carries current so well.", "(c…)", "copper"),
 G("Her engagement ring is ___, a white metal even rarer than gold.", "(p…)", "platinum"),
 G("The ___ on the ring is so hard that it can cut glass.", "(d…)", "diamond"),
 G("The old factory is built of red ___, and it now houses a design school.", "(b…)", "brick", ["brick","bricks"]),
 G("Matteo carved a small ___ spoon from a piece of olive branch.", "(w…)", "wooden"),
 G("On the farm the cows sleep on fresh ___ in the barn.", "(s…)", "straw"),
 G("The benches in our park are ___ plastic: two thousand old bottles went into each one.", "(r…)", "recycled"),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — tessuti e materiali",
 desc="i primi due livelli insieme · frasi e definizioni nuove", items=[
 D("«the soft hair of sheep, spun into thread for jumpers and socks» → ___", "(w…)", "wool"),
 G("These ___ cushions feel so soft that the cat sleeps on them all day.", "(v…)", "velvet"),
 G("Antonella's tablecloth has a ___ border with a pattern of tiny roses and holes.", "(l…)", "lace"),
 D("«a strong blue cloth that is perfect for work trousers and jackets» → ___", "(d…)", "denim"),
 G("At the nature centre the children watched a ___ slowly wrap itself in a cocoon of shiny thread.", "(s…)", "silkworm", ["silkworm","silk worm"]),
 G("These sofas look like real animal skin, but they're covered in ___ made from cactus.", "(e… l…)", "eco-friendly leather", ["eco-friendly leather","eco friendly leather","eco-leather","eco leather"]),
 D("«a precious stone that is the hardest natural material on Earth» → ___", "(d…)", "diamond", ["diamond","diamonds"]),
 G("The pipes in my grandmother's house are ___: you can tell from their orange-brown colour.", "(c…)", "copper"),
 G("In the story, the first little pig builds his house of ___, and the wolf blows it down in a second.", "(s…)", "straw"),
 D("«a rectangular red block that builders put in rows with cement» → ___", "(b…)", "brick", ["brick","bricks"]),
 G("The pages of my diary are ___ paper: they were once a pile of old newspapers.", "(r…)", "recycled"),
 G("My uncle makes ___ toys for his grandchildren — horses, trains and boats, all from old planks.", "(w…)", "wooden"),
 D("«a shiny, very valuable white metal; jewellers use it for expensive wedding rings» → ___", "(p…)", "platinum"),
 G("Mum keeps her best ___ blouse for weddings: it's so delicate that she washes it by hand.", "(s…)", "silk", ["silk","satin"]),
 G("After twenty years the ___ on Dad's armchair is cracked and dark, but he won't change it.", "(l…)", "leather"),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — SHAPES AND PATTERNS",
 desc="a righe, a pois · a forma di cuore o di stella · triangolare · diagonale, orizzontale, verticale", rule=RULE, items=[
 D("«with long, narrow bands of different colours, like a zebra» → ___", "(s…)", "striped", ["striped","stripy","stripey"]),
 D("«covered with small round marks, like a ladybird» → ___", "(s…)", "spotted", ["spotted","spotty"]),
 D("«with the form of the symbol of love» → ___", "(h…-s…)", "heart-shaped", ["heart-shaped","heart shaped"]),
 D("«with five or more points, like the ones in the night sky» → ___", "(s…-s…)", "star-shaped", ["star-shaped","star shaped"]),
 D("«with three straight sides and three corners» → ___", "(t…)", "triangular"),
 D("«a straight line that joins two opposite corners of a square or a rectangle» → ___", "(d…)", "diagonal"),
 D("«flat and level, parallel to the ground» → ___", "(h…)", "horizontal"),
 D("«going straight up, at ninety degrees to the ground» → ___", "(v…)", "vertical"),
 G("Sailors in old films often wear blue and white ___ T-shirts.", "(s…)", "striped", ["striped","stripy","stripey"]),
 G("My little brother wants a ___ bow tie for the wedding, black with tiny white dots.", "(s…)", "spotted", ["spotted","spotty"]),
 G("Elsa cut the pizza dough into small ___ pieces for her parents' anniversary.", "(h…-s…)", "heart-shaped", ["heart-shaped","heart shaped"]),
 G("At Christmas the shop sells little ___ lights with five points to hang in the window.", "(s…-s…)", "star-shaped", ["star-shaped","star shaped"]),
 G("Road signs that warn you of a danger are ___ in Italy, with a red border.", "(t…)", "triangular"),
 G("Cross the square in a ___ line: it's quicker than walking round the edges.", "(d…)", "diagonal"),
 G("Hang the picture with a spirit level, so that it's perfectly ___.", "(h…)", "horizontal"),
 G("The climbers stopped at the bottom of an almost ___ wall of rock.", "(v…)", "vertical"),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — AGE, TEXTURE AND FIT",
 desc="antico, di seconda mano · soffice · su misura", rule=RULE, items=[
 D("«measuring a long distance from one side to the other» → ___", "(w…)", "wide"),
 D("«going a long way down from the top or the surface» → ___", "(d…)", "deep"),
 D("«with a large distance between the two opposite surfaces, like a heavy book or a winter blanket» → ___", "(t…)", "thick"),
 D("«old and valuable, often a piece of furniture made more than a hundred years ago» → ___", "(a…)", "antique"),
 D("«already used by someone else before you bought it» → ___", "(s…-h…)", "second-hand", ["second-hand","second hand","secondhand"]),
 D("«soft and light, covered in fine hair or feathers, like a kitten» → ___", "(f…)", "fluffy"),
 D("«made specially to fit one particular person's body» → ___", "(m… t… m…)", "made to measure", ["made to measure","made-to-measure"]),
 G("The river here is about fifty metres ___, so the new bridge has three arches.", "(w…)", "wide"),
 G("Don't dive at that end of the pool: it's only one metre ___.", "(d…)", "deep"),
 G("The castle walls are so ___ that the windows look like small tunnels.", "(t…)", "thick"),
 G("Grandma's ___ clock belonged to her great-grandfather, and a dealer offered her a fortune for it.", "(a…)", "antique"),
 G("I bought this bike ___ from a neighbour for forty euros; it's ten years old, but it works perfectly.", "(s…-h…)", "second-hand", ["second-hand","second hand","secondhand"]),
 G("The baby owl looked like a small ___ ball of grey feathers.", "(f…)", "fluffy"),
 G("Grandpa's wedding suit was ___ by a tailor in Treviso, so it fits him perfectly.", "(m… t… m…)", "made to measure", ["made to measure","made-to-measure"]),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — INVENTIONS AND NEW PRODUCTS",
 desc="prototipo · laboratorio, fisico · lancio, dimostrazione · in vendita, per caso, gratis", rule=RULE, items=[
 D("«to design or create something that did not exist before» → ___", "(i…)", "invent"),
 D("«a person who designs or creates a new machine or process» → ___", "(i…)", "inventor"),
 D("«the first model of a new product, built to test it before making many copies» → ___", "(p…)", "prototype"),
 D("«a room or building with special equipment where scientists do tests» → ___", "(l…)", "laboratory", ["laboratory","lab"]),
 D("«a scientist who studies energy, light, heat and the forces of nature» → ___", "(p…)", "physicist"),
 D("«cloth with tiny sensors or electronics inside it, for example to measure your heart rate» → ___", "(s… f…)", "smart fabric", ["smart fabric","smart fabrics"]),
 D("«an event where someone shows people how a new product works» → ___", "(d…)", "demonstration", ["demonstration","demo"]),
 D("«to become available for people to buy in shops» → ___", "(g… o… s…)", "go on sale"),
 D("«without planning it or wanting it» → ___", "(b… a…)", "by accident"),
 D("«without paying any money» → ___", "(f… f…)", "for free"),
 D("«the event when a company presents a new product to the public for the first time» → ___", "(l…)", "launch"),
 G("Nobody knows who ___ the wheel, but it changed transport forever.", "(i…)", "invented"),
 G("My great-uncle was an ___: he designed a machine that peels twenty oranges a minute.", "(i…)", "inventor"),
 G("The students built a ___ of their solar charger from a shoebox and a small panel, and tested it in the yard.", "(p…)", "prototype"),
 G("The chemistry ___ is closed today because someone broke a lot of test tubes.", "(l…)", "laboratory", ["laboratory","lab"]),
 G("Sofia is a ___: at the university she studies how light travels through different materials.", "(p…)", "physicist"),
 G("The marathon runners wear shirts made of a ___ that measures their heartbeat and sends the data to their phones.", "(s… f…)", "smart fabric"),
 G("At the science fair a girl gave a ___ of her robot vacuum cleaner, and it cleaned the whole stage.", "(d…)", "demonstration", ["demonstration","demo"]),
 G("The new console ___ next Friday; fans are already queuing outside the shop.", "(verbo + on s…)", "goes on sale", ["goes on sale","will go on sale","is going on sale"]),
 G("Penicillin was discovered ___: a scientist left some dishes uncovered before a holiday.", "(b… a…)", "by accident"),
 G("Students under eighteen can visit the museum ___ on the first Sunday of the month.", "(f… f…)", "for free"),
 G("Hundreds of journalists came to the ___ of the new electric car in Turin.", "(l…)", "launch"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — forme, misure, invenzioni",
 desc="livelli 3-5 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«straight up and down, like the walls of a tall building» → ___", "(v…)", "vertical"),
 G("Our club flag has three ___ stripes: green at the top, white in the middle and red at the bottom.", "(h…)", "horizontal"),
 G("In chess the bishop can only move in a ___ line.", "(d…)", "diagonal"),
 D("«with the shape that people draw on Valentine's cards» → ___", "(h…-s…)", "heart-shaped", ["heart-shaped","heart shaped"]),
 G("The pyramids of Egypt have four ___ sides that meet at the top.", "(t…)", "triangular"),
 D("«having lines of different colours, like a deckchair or a bee» → ___", "(s…)", "striped", ["striped","stripy","stripey"]),
 G("— How ___ is the lake? — About forty metres in the middle, so don't swim out too far.", "(d…)", "deep"),
 D("«soft and full of air, like a newly washed towel or the feathers of a baby chick» → ___", "(f…)", "fluffy"),
 G("This bookcase is ___: it was made in Venice around 1850, and it's worth a lot.", "(a…)", "antique"),
 G("The shop on the corner sells only ___ clothes, so you can find a designer coat for twenty euros.", "(s…-h…)", "second-hand", ["second-hand","second hand","secondhand"]),
 D("«the person who first has the idea for a new machine and designs it» → ___", "(i…)", "inventor"),
 G("The concert tickets ___ at nine tomorrow morning, and they'll probably sell out in minutes.", "(verbo + on s…)", "go on sale", ["go on sale","will go on sale","are going on sale"]),
 G("I found my favourite café completely ___: I took a wrong turn on the way home.", "(b… a…)", "by accident"),
 G("A team of engineers is testing the ___ in a secret workshop: if it works, the factory will make a million copies.", "(p…)", "prototype"),
 D("«a scientist who studies how matter, energy and movement work» → ___", "(p…)", "physicist"),
 G("Children under six travel ___ on the city buses.", "(f… f…)", "for free"),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Made to measure",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 G("Elena knitted me a ___ hat for the mountains, soft and very warm.", "(w…)", "woollen", ["woollen","woolen","wool"]),
 D("«a cloth with a deep, soft surface, a favourite for theatre curtains» → ___", "(v…)", "velvet"),
 G("Her grandmother's wedding dress has long ___ sleeves, so delicate that you can see her arms through them.", "(l…)", "lace"),
 G("The roof of the old church turned green over the centuries because it's covered in ___.", "(c…)", "copper"),
 G("We got this sofa ___ from a neighbour who was moving abroad.", "(f… f…)", "for free"),
 D("«a long line that goes from the top left corner of a page to the bottom right» → ___", "(d…)", "diagonal"),
 G("The wardrobe is too ___ for the corridor: we need to take the doors off to get it in.", "(w…)", "wide"),
 G("Ilaria has very long arms, so all her shirts are ___: the ones in normal shops are always too short.", "(m… t… m…)", "made to measure", ["made to measure","made-to-measure"]),
 D("«the first working version of a machine, before the factory produces it» → ___", "(p…)", "prototype"),
 G("All the bags in this shop are ___: they were once fishing nets and old tyres.", "(r…)", "recycled"),
 G("Seen from the plane, the fields look like a ___ tablecloth: green, yellow, green, yellow.", "(s…)", "striped", ["striped","stripy","stripey"]),
 G("The new trainers ___ at midnight, and the website crashed after ten minutes.", "(verbo + on s…)", "went on sale"),
 D("«a material for clothes with tiny electronic parts that react to your body» → ___", "(s… f…)", "smart fabric", ["smart fabric","smart fabrics"]),
 G("Our science teacher took us to the university ___ to see a real electron microscope.", "(l…)", "laboratory", ["laboratory","lab"]),
 G("A big golden ___ decoration with five points sits on top of the Christmas tree.", "(s…-s…)", "star-shaped", ["star-shaped","star shaped"]),
 D("«with a pattern of dots of a different colour, like a Dalmatian dog» → ___", "(s…)", "spotted", ["spotted","spotty"]),
 G("The ice on the pond is only a few centimetres ___, so nobody can skate on it yet.", "(t…)", "thick"),
 G("The ring has a tiny ___ in the middle that sparkles in the light.", "(d…)", "diamond"),
 G("The Chinese ___ paper about two thousand years ago, using tree bark and old fishing nets.", "(i…)", "invented"),
]))

GLOSS = {
 "silk":"seta","caterpillar":"bruco","threads":"fili","thread":"filo","cloth":"tessuto, stoffa","shiny":"lucido",
 "silkworm":"baco da seta","cocoon":"bozzolo","mulberry":"gelso","mills":"setifici, stabilimenti","velvet":"velluto",
 "cushions":"cuscini","fur":"pelliccia, pelo","lace":"pizzo, merletto","veil":"velo","tablecloths":"tovaglie",
 "tablecloth":"tovaglia","denim":"tessuto jeans, denim","leather":"pelle, cuoio","tannery":"conceria","harming":"far del male a",
 "eco-friendly leather":"ecopelle","peel":"buccia","woollen":"di lana","wool":"lana","sheep":"pecore","jumper":"maglione",
 "copper":"rame","reddish-brown":"bruno-rossastro","wires":"fili elettrici","current":"corrente","platinum":"platino",
 "engagement ring":"anello di fidanzamento","diamond":"diamante","precious stone":"pietra preziosa","brick":"mattone",
 "bricks":"mattoni","clay":"argilla","baked":"cotto","cement":"cemento","wooden":"di legno","carved":"intagliato",
 "branch":"ramo","straw":"paglia","stems":"steli","wheat":"grano","barn":"stalla, fienile","recycled":"riciclato",
 "bench":"panchina","pile":"mucchio","planks":"assi di legno","pipes":"tubi","jewellers":"gioiellieri","blouse":"camicetta",
 "satin":"raso","armchair":"poltrona","cracked":"screpolato","striped":"a righe","stripes":"strisce","bands":"fasce",
 "spotted":"a pois, maculato","ladybird":"coccinella","dots":"puntini, pois","bow tie":"farfallino","heart-shaped":"a forma di cuore",
 "star-shaped":"a forma di stella","dough":"impasto","triangular":"triangolare","border":"bordo","diagonal":"diagonale",
 "edges":"bordi","horizontal":"orizzontale","spirit level":"livella","vertical":"verticale","bishop":"alfiere",
 "deckchair":"sdraio","wide":"largo","deep":"profondo","thick":"spesso","arches":"arcate","dive":"tuffarsi",
 "antique":"antico, d'antiquariato","dealer":"antiquario, commerciante","second-hand":"di seconda mano, usato",
 "fluffy":"soffice, vaporoso","owl":"gufo","feathers":"piume","chick":"pulcino","made to measure":"su misura",
 "tailor":"sarto","nature centre":"centro di educazione ambientale","invent":"inventare","invented":"inventò, ha inventato","inventor":"inventore",
 "prototype":"prototipo","charger":"caricabatterie","laboratory":"laboratorio","lab":"laboratorio","test tubes":"provette",
 "physicist":"fisico","smart fabric":"tessuto intelligente","sensors":"sensori","heartbeat":"battito cardiaco",
 "demonstration":"dimostrazione","vacuum cleaner":"aspirapolvere","go on sale":"essere messo in vendita",
 "goes on sale":"viene messo in vendita","went on sale":"è stato messo in vendita","queuing":"in coda",
 "by accident":"per caso, per sbaglio","penicillin":"penicillina","uncovered":"scoperti","for free":"gratis",
 "launch":"lancio, presentazione","peels":"sbuccia","matter":"materia","wardrobe":"armadio","tyres":"pneumatici",
 "pond":"laghetto","sparkles":"brilla","knitted":"ha fatto a maglia","bark":"corteccia","sleeves":"maniche",
}

# Schede di studio: [voce, definizione inglese, esempio nuovo, italiano] (+ True per i chunk da coprire interi)
STUDY = {
"1": [
 ["silk", "a soft, smooth, shiny cloth made from the threads that a small caterpillar produces", "My aunt brought me a silk tie from China.", "seta"],
 ["silkworm", "a small caterpillar that wraps itself in a cocoon of fine thread", "Farmers in Japan still raise silkworms in wooden trays.", "baco da seta"],
 ["velvet", "a heavy cloth with a thick, very soft surface", "Velvet curtains keep the cold out in winter.", "velluto"],
 ["lace", "a delicate cloth with a pattern of small holes", "She wore white lace gloves at the ceremony.", "pizzo, merletto"],
 ["denim", "a strong cotton cloth, usually blue, used to make jeans", "A denim jacket goes well with almost everything.", "tessuto jeans, denim"],
 ["leather", "animal skin that is treated and used to make shoes, bags, belts and jackets", "Leather shoes last longer if you clean them often.", "pelle, cuoio"],
 ["eco-friendly leather", "a material that looks like animal skin but is produced without harming any animals", "Eco-friendly leather can come from mushrooms or grape skins.", "ecopelle"],
 ["woollen", "made of the soft, thick hair of sheep", "In winter I sleep under a heavy woollen blanket.", "di lana"],
],
"2": [
 ["copper", "a reddish-brown metal that carries electricity well and turns green with time", "The old saucepans in our kitchen are copper.", "rame"],
 ["platinum", "a rare, heavy, silver-white precious metal, used for rings and in car parts", "A platinum watch is heavier than a steel one.", "platino"],
 ["diamond", "a very hard, clear precious stone, often used in engagement rings", "Glass cutters often have a tiny diamond at the tip.", "diamante"],
 ["brick", "a hard block of baked clay used to build walls and houses", "Many houses in London are built of brick.", "mattone"],
 ["wooden", "made of the hard material that comes from trees", "We ate at a long wooden table under the trees.", "di legno"],
 ["straw", "dry yellow stems of wheat, used for summer hats, baskets and animal beds", "The horses need clean straw in their stable.", "paglia"],
 ["recycled", "made again from things that people threw away", "Our school prints its posters on recycled paper.", "riciclato"],
],
"3": [
 ["striped", "with long, narrow bands of different colours, like a zebra", "Bees have striped bodies, black and yellow.", "a righe"],
 ["spotted", "covered with small round marks, like a ladybird", "A leopard has a spotted coat.", "a pois, maculato"],
 ["heart-shaped", "with the form of the symbol of love", "She keeps her earrings in a heart-shaped box.", "a forma di cuore"],
 ["star-shaped", "with five or more points, like the ones in the night sky", "He bought a star-shaped cake tin for the party.", "a forma di stella"],
 ["triangular", "with three straight sides and three corners", "A slice of pizza is roughly triangular.", "triangolare"],
 ["diagonal", "going from one corner of a square to the opposite corner", "Draw a diagonal across the rectangle with a ruler.", "diagonale"],
 ["horizontal", "flat and level, parallel to the ground", "The flag of Austria has three horizontal bands.", "orizzontale"],
 ["vertical", "going straight up, at ninety degrees to the ground", "This cliff is almost vertical, so only experts climb it.", "verticale"],
],
"4": [
 ["wide", "measuring a long distance from one side to the other", "The new motorway is wide enough for four lanes.", "largo"],
 ["deep", "going a long way down from the top or the surface", "The lake near our village is deep and cold.", "profondo"],
 ["thick", "with a large distance between the two opposite surfaces", "That dictionary is so thick that it doesn't fit in my bag.", "spesso"],
 ["antique", "old and valuable, often a piece of furniture made more than a hundred years ago", "They sell antique furniture in a shop near the cathedral.", "antico, d'antiquariato"],
 ["second-hand", "already used by someone else before you bought it", "Second-hand books are cheaper and often in good condition.", "di seconda mano, usato"],
 ["fluffy", "soft and light, covered in fine hair or feathers", "The puppy has fluffy ears and a short tail.", "soffice, vaporoso"],
 ["made to measure", "made specially to fit one particular person's body", "The curtains in the hotel were made to measure for the huge windows.", "su misura"],
],
"5": [
 ["invent", "to design or create something that did not exist before", "Two students invented an app that helps blind people cross the road.", "inventare"],
 ["inventor", "a person who designs or creates a new machine or process", "The inventor of the board game was a teacher who wanted to make maths fun.", "inventore"],
 ["prototype", "the first model of a new product, built to test it before making many copies", "The first prototype of the drone crashed after ten seconds.", "prototipo"],
 ["laboratory", "a room or building with special equipment where scientists do tests", "Our school laboratory has some new microscopes.", "laboratorio"],
 ["physicist", "a scientist who studies energy, light, heat and the forces of nature", "Her mother is a physicist who works on solar energy.", "fisico"],
 ["smart fabric", "cloth with tiny sensors or electronics inside it", "Smart fabric can change colour when the temperature changes.", "tessuto intelligente"],
 ["demonstration", "an event where someone shows people how a new product works", "The salesman gave a quick demonstration of the coffee machine.", "dimostrazione"],
 ["go on sale", "to become available for people to buy in shops", "The new phone goes on sale in Europe next month.", "essere messo in vendita", True],
 ["by accident", "without planning it or wanting it", "I deleted all my holiday photos by accident.", "per caso, per sbaglio"],
 ["for free", "without paying any money", "You can download the app for free.", "gratis"],
 ["launch", "the event when a company presents a new product to the public for the first time", "The launch of the new game is on Saturday in Milan.", "lancio, presentazione"],
],
}

# voci di base tolte nella revisione (decisione: niente lessico del primo/secondo anno)
_BASE = {"wide", "deep", "thick", "invent", "invented", "inventor"}
for _L in LEVELS:
    _L["items"] = [it for it in _L["items"] if it[3].lower() not in _BASE]
for _k in STUDY:
    STUDY[_k] = [r for r in STUDY[_k] if r[0].lower() not in _BASE]
