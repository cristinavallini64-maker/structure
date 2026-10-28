# Contenuti del lessico, Unit 5 "No Planet B"
from lexlib import *
UNIT = 5
NAME = "No Planet B"
TOPICS = "natural disasters · extreme and everyday weather · climate change and energy · nature in danger · green habits and Real Talk"
META = "natural disasters, weather, climate change, energy and the environment"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — NATURAL DISASTERS",
 desc="terremoti, tsunami, eruzioni · frane, valanghe, alluvioni, incendi", rule=RULE, items=[
 D("«a sudden, violent shaking of the ground, caused by movements deep inside the Earth» → ___", "(e…)", "earthquake"),
 D("«a huge sea wave, often produced by an earthquake under the ocean, that floods the coast» → ___", "(t…)", "tsunami"),
 D("«the moment when a mountain throws out hot rock, ash and gas» → ___", "(v… e…)", "volcanic eruption"),
 D("«a mass of earth and rocks that suddenly falls down the side of a hill» → ___", "(l…)", "landslide", ["landslide","landslip"]),
 D("«a large amount of snow and ice that falls suddenly down a mountain» → ___", "(a…)", "avalanche"),
 D("«a large amount of water that covers an area which is usually dry» → ___", "(f…)", "flood", ["flood","flooding"]),
 D("«flames that spread quickly and out of control through forests or dry grass» → ___", "(w…)", "wildfire", ["wildfire","wild fire","wildfires"]),
 D("«(of a river) so full that the water goes over its banks» → ___", "(i… f…)", "in flood"),
 G("In 1976 a strong ___ shook Friuli and destroyed whole villages in less than a minute.", "(e…)", "earthquake"),
 G("After the shaking stopped, the sirens warned people on the beach to run uphill: a ___ was on its way.", "(t…)", "tsunami"),
 G("In 2010 a ___ in Iceland sent a huge cloud of ash into the sky, and thousands of flights stayed on the ground.", "(v… e…)", "volcanic eruption"),
 G("After a week of heavy rain, a ___ blocked the mountain road with mud and rocks.", "(l…)", "landslide", ["landslide","landslip"]),
 G("Mountain guides have closed the north side of the valley: after two metres of fresh snow, the danger of an ___ is very high.", "(a…)", "avalanche"),
 G("When the river burst its banks, the ___ filled the ground floor of our house with mud.", "(f…)", "flood", ["flood","flooding","floodwater","floodwaters"]),
 G("In August a ___ destroyed hundreds of hectares of pine forest along the coast.", "(w…)", "wildfire", ["wildfire","wild fire"]),
 G("Don't cross the old wooden bridge today: the river is ___ and the water has almost reached the planks.", "(i… f…)", "in flood"),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — STORMS AND EXTREME WEATHER",
 desc="uragani, tifoni, bufere di neve · grandine, fulmini, burrasche · siccità e ondate di calore", rule=RULE, items=[
 D("«a violent storm with very strong winds that forms over the Atlantic Ocean» → ___", "(h…)", "hurricane"),
 D("«a violent tropical storm with very strong winds in the western Pacific, for example near Japan or the Philippines» → ___", "(t…)", "typhoon"),
 D("«a snowstorm with strong winds, so you can see almost nothing» → ___", "(b…)", "blizzard"),
 D("«small balls of ice that fall from the sky like rain» → ___", "(h…)", "hail", ["hail","hailstones"]),
 D("«the sudden flash of bright light in the sky during a storm» → ___", "(l…)", "lightning"),
 D("«a very strong wind that blows for hours» → ___", "(g…)", "gale", ["gale","gales"]),
 D("«long periods with little or no rain, when rivers and fields dry up» → ___", "(d…)", "droughts", ["droughts","drought"]),
 D("«a period of days or weeks when the weather is much hotter than usual» → ___", "(h…)", "heatwave", ["heatwave","heat wave"]),
 G("The ___ reached Florida at night with winds of over 200 kilometres an hour.", "(h…)", "hurricane"),
 G("In September the ___ season begins in the Philippines: strong winds and heavy rain can go on for days.", "(t…)", "typhoon"),
 G("We couldn't see the car in front of us: the ___ covered the motorway with snow in twenty minutes.", "(b…)", "blizzard"),
 G("In ten minutes the ___ smashed the glass roof of the greenhouse: some pieces of ice were the size of walnuts.", "(h…)", "hail", ["hail","hailstorm","hailstones"]),
 G("During the storm, ___ hit the old oak in the square and split it in two.", "(l…)", "lightning"),
 G("No ferries will sail to the islands tomorrow: the forecast says a ___ is coming from the north.", "(g…)", "gale"),
 G("Southern Spain has had several serious ___ in the last ten years, and some villages now get their water from lorries.", "(d…)", "droughts"),
 G("During the ___ in July, temperatures stayed above 38 degrees for ten days and the hospitals filled up.", "(h…)", "heatwave", ["heatwave","heat wave"]),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — EVERYDAY WEATHER",
 desc="brezza, clima mite, brina · terre aride, ghiaccio sulla strada · bagnati fradici e scottati", rule=RULE, items=[
 D("«a light, pleasant wind» → ___", "(b…)", "breeze"),
 D("«(of weather, especially in winter) not too cold and quite pleasant» → ___", "(m…)", "mild"),
 D("«a thin white layer of ice on grass and cars on very cold mornings» → ___", "(f…)", "frost"),
 D("«so dry that almost no plants can grow there» → ___", "(a…)", "arid"),
 D("«a dangerous, almost invisible frozen layer on the road in winter, which makes cars skid» → ___", "(b… i…)", "black ice"),
 D("«completely wet, for example after walking in heavy rain» → ___", "(s…)", "soaked", ["soaked","sodden"]),
 D("«with red, painful skin after too much time in the sun» → ___", "(s…)", "sunburnt", ["sunburnt","sunburned"]),
 G("It's hot in the city, but on our terrace there's always a cool ___ from the lake in the evening.", "(b…)", "breeze"),
 G("It was a ___ winter: we turned the heating on only twice and the roses flowered in January.", "(m…)", "mild"),
 G("There was ___ on the windscreen this morning, so I had to scrape it off before driving to work.", "(f…)", "frost"),
 G("Few plants survive in this ___ land: it gets less than 100 millimetres of rain a year.", "(a…)", "arid"),
 G("Drive slowly on the mountain road this morning: there's ___ on the bends and you can't see it.", "(b… i…)", "black ice"),
 G("I forgot my umbrella and got ___ on the way home — even my socks were wet.", "(s…)", "soaked", ["soaked","sodden"]),
 G("Lorenzo fell asleep on the sunbed at noon, and now his shoulders hurt: he's badly ___.", "(s…)", "sunburnt", ["sunburnt","sunburned"]),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — disastri naturali e tempo atmosferico",
 desc="i primi tre livelli insieme · frasi e definizioni nuove", items=[
 D("«a sudden, dangerous fall of snow down a steep slope» → ___", "(a…)", "avalanche"),
 G("The ___ in Haiti in 2010 lasted only thirty-five seconds, but it destroyed much of the capital.", "(e…)", "earthquake"),
 D("«a giant wave that can travel across a whole ocean at the speed of a plane» → ___", "(t…)", "tsunami"),
 G("Firefighters and planes worked for three days to stop the ___ before it reached the village.", "(w…)", "wildfire", ["wildfire","wild fire"]),
 D("«a storm with lots of snow and wind so strong that roads close and cars get stuck» → ___", "(b…)", "blizzard"),
 G("Our tent shook all night in the ___: the wind snapped one of the poles.", "(g…)", "gale", ["gale","gales"]),
 D("«ice that falls from storm clouds in small hard balls» → ___", "(h…)", "hail", ["hail","hailstones"]),
 G("Never stand under a tree in a storm: ___ often hits the tallest thing around.", "(l…)", "lightning"),
 G("The ___ lasted two weeks: fourteen days in a row of more than 38 degrees in the shade, and the city streets were empty.", "(h…)", "heatwave", ["heatwave","heat wave"]),
 D("«a soft, gentle movement of air, often near the sea» → ___", "(b…)", "breeze"),
 G("The ___ on the lawn this morning was white and crunchy, and the kids drew pictures in it with their fingers.", "(f…)", "frost"),
 D("«(of a winter) warmer than normal, without snow or hard frosts» → ___", "(m…)", "mild"),
 G("Our hike turned into a disaster: we walked four hours in the storm and arrived at the hut completely ___.", "(s…)", "soaked", ["soaked","sodden"]),
 G("A ___ swept away part of the hillside road, and the bus to the village now takes a long detour.", "(l…)", "landslide", ["landslide","landslip"]),
 G("After an hour in the midday sun without a hat, Nico's nose was bright red: he was badly ___.", "(s…)", "sunburnt", ["sunburnt","sunburned"]),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — CLIMATE CHANGE AND ENERGY",
 desc="ghiacciai e calotte polari · effetto serra, emissioni · combustibili fossili ed energia rinnovabile", rule=RULE, items=[
 D("«a large mass of ice that moves very slowly down a mountain valley» → ___", "(g…)", "glacier"),
 D("«the thick layers of ice that cover the land near the North and South Poles» → ___", "(i… c…)", "ice caps", ["ice caps","ice cap","icecaps"]),
 D("«the average height of the sea, used to measure the height of mountains» → ___", "(s… l…)", "sea level", ["sea level","sea levels"]),
 D("«the warming of the Earth because gases in the air keep the sun's heat in» → ___", "(g… e…)", "greenhouse effect"),
 D("«the gas that we breathe out and that cars and factories produce when they burn fuel; its formula is CO2» → ___", "(c… d…)", "carbon dioxide"),
 D("«the part of the upper atmosphere that protects us from the sun's dangerous ultraviolet rays» → ___", "(o… l…)", "ozone layer"),
 D("«gases like CO2 that cars, planes and factories send into the air» → ___", "(e…)", "emissions"),
 D("«coal, oil and gas: sources of energy formed from plants and animals that died millions of years ago» → ___", "(f… f…)", "fossil fuels"),
 D("«the slow rise in the average temperature of the Earth» → ___", "(g… w…)", "global warming"),
 D("«power from sources that never run out, like the sun, the wind and water» → ___", "(r… e…)", "renewable energy"),
 D("«flat pieces of equipment on a roof that turn sunlight into electricity» → ___", "(s… p…)", "solar panels", ["solar panels","solar panel"]),
 G("Fifty years ago the ___ reached the hut; now you have to walk an hour uphill to touch the ice.", "(g…)", "glacier"),
 G("Satellite photos show that the polar ___ are getting smaller each summer.", "(i… c…)", "ice caps", ["ice caps","icecaps"]),
 G("Venice is only a metre above ___, so even a small rise might put St Mark's Square under water.", "(s… l…)", "sea level"),
 G("In our science lesson we built a model of the ___ with two jars, a lamp and a thermometer.", "(g… e…)", "greenhouse effect"),
 G("Trees take in ___ from the air and give back oxygen.", "(c… d…)", "carbon dioxide"),
 G("In the 1980s scientists discovered a hole in the ___ above Antarctica.", "(o… l…)", "ozone layer"),
 G("The city wants to cut traffic ___ by half, so diesel cars can't enter the centre from next year.", "(e…)", "emissions"),
 G("Most power stations in Poland still ___, mainly coal, and the smoke from their chimneys makes the winter air terrible.", "(verbo + f… f…)", "burn fossil fuels", ["burn fossil fuels","use fossil fuels","rely on fossil fuels","run on fossil fuels","depend on fossil fuels"]),
 G("Scientists agree that ___ is the main reason why the Alps are losing their snow.", "(g… w…)", "global warming"),
 G("Our school plans to ___ by 2030: wind turbines on the hill and no more gas boilers.", "(verbo + to r… e…)", "switch to renewable energy", ["switch to renewable energy","move to renewable energy","change to renewable energy","turn to renewable energy","convert to renewable energy","go over to renewable energy"]),
 G("The farm next door covered the old barn roof with ___: on sunny days it sells electricity to the grid.", "(s… p…)", "solar panels"),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — NATURE AND WATER IN DANGER",
 desc="specie a rischio ed estinte · barriere coralline · bacini e carenza d'acqua · vigneti e raccolti", rule=RULE, items=[
 D("«a type of animal or plant that may soon disappear from the Earth forever» → ___", "(e… s…)", "endangered species"),
 D("«(of an animal or plant) with no members alive today, like the dinosaurs» → ___", "(e…)", "extinct"),
 D("«a long line of colourful rock-like structures under warm seas, built by tiny sea animals» → ___", "(c… r…)", "coral reef"),
 D("«an artificial lake that stores water for a town or for farms» → ___", "(r…)", "reservoir"),
 D("«a situation in which there is not enough water for everyone» → ___", "(w… s…)", "water shortage", ["water shortage","water shortages"]),
 D("«a piece of land where grapes grow, usually to make wine» → ___", "(v…)", "vineyard"),
 D("«the time when farmers collect their crops, or the crops that they collect» → ___", "(h…)", "harvest"),
 G("There are only about a thousand mountain gorillas left in the wild: they are an ___.", "(e… s…)", "endangered species"),
 G("The dodo became ___ about 350 years ago, not long after sailors arrived on its island.", "(e…)", "extinct"),
 G("Warmer seas are turning the ___ near the Maldives white, and the fish that live there are disappearing.", "(c… r…)", "coral reef", ["coral reef","coral reefs"]),
 G("After the dry winter, the ___ above the town is only a third full, and the council is asking people to save water.", "(r…)", "reservoir"),
 G("Farmers in Sicily are worried about ___: the wells are almost dry and it hasn't rained since March.", "(w… s…)", "water shortages", ["water shortages","water shortage"]),
 G("My uncle's ___ on the hills near Valdobbiadene produces grapes for Prosecco.", "(v…)", "vineyard"),
 G("After the hailstorm in June, this year's apple ___ is half the usual size.", "(h…)", "harvest"),
]))

# ---------------------------------------------------------------- 06
LEVELS.append(dict(id=6, type="study", title="LIVELLO 06 — GREEN HABITS AND REAL TALK",
 desc="impronta di carbonio, compensazione, greenwashing · compost, standby, car sharing · espressioni colloquiali", rule=RULE, items=[
 D("«the total amount of CO2 that a person or an activity produces» → ___", "(c… f…)", "carbon footprint"),
 D("«paying for projects, like planting trees, to balance the CO2 that you produce» → ___", "(c… o…)", "carbon offsetting", ["carbon offsetting","carbon offset"]),
 D("«when a company pretends that its products are better for the environment than they really are» → ___", "(g…)", "greenwashing", ["greenwashing","green washing","green-washing"]),
 D("«a mix of dead leaves and food waste that rots and makes the soil rich» → ___", "(c…)", "compost"),
 D("«(of bags, cups or bottles) that you keep for a long time, not throw away after one go» → ___", "(r…)", "reusable", ["reusable","re-usable"]),
 D("«the mode of a TV or computer that is off but still uses a little electricity» → ___", "(s…)", "standby", ["standby","stand-by"]),
 D("«a service with cars parked around the city that members can rent by the minute or by the hour» → ___", "(c…)", "car-sharing", ["car-sharing","car sharing","carsharing"]),
 D("«a large container in the garden that collects rain from the roof» → ___", "(w… b…)", "water butt"),
 D("«to do something good so that a bad thing seems less bad» → ___", "(m… u… f…)", "make up for"),
 D("«(of a bad situation) to become even more serious» → ___", "(g… f… b… t… w…)", "go from bad to worse"),
 D("«to believe something that is not true because you want to believe it» → ___", "(k… y…)", "kid yourself"),
 G("Eating less meat is one easy way to ___: beef needs a lot of land and water.", "(verbo + your c… f…)", "reduce your carbon footprint", ["reduce your carbon footprint","cut your carbon footprint","lower your carbon footprint","shrink your carbon footprint"]),
 G("Some airlines offer ___: you pay ten euros more and they plant trees in Kenya.", "(c… o…)", "carbon offsetting", ["carbon offsetting","carbon offset"]),
 G("The ad shows green fields and happy cows, but the company still pollutes the river: it's pure ___.", "(g…)", "greenwashing", ["greenwashing","green washing","green-washing"]),
 G("We put fruit peel and coffee grounds in a bin at the end of the garden, and in spring we use the ___ on the tomatoes.", "(c…)", "compost"),
 G("Mum keeps three ___ cloth bags in the boot, so she never needs plastic ones at the checkout.", "(r…)", "reusable", ["reusable","re-usable"]),
 G("The little red light on the TV means it's on ___ and still using power.", "(s…)", "standby", ["standby","stand-by"]),
 G("Paola sold her old car: now she uses a ___ app and books a small electric car only when she needs one.", "(c…)", "car-sharing", ["car-sharing","car sharing","carsharing"]),
 G("Our ___ collected 200 litres during the storm: enough for the flower pots for a month.", "(w… b…)", "water butt"),
 G("Planting one tree doesn't ___ three flights a year.", "(m… u… f…)", "make up for"),
 G("First the cellar filled with water, then the electricity went off; on Sunday things ___ when part of the roof fell in.", "(verbo + from b… to w…)", "went from bad to worse"),
 G("If you think a few paper straws can save the oceans, you're ___.", "(k… y…)", "kidding yourself"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — clima, natura e abitudini verdi",
 desc="livelli 4-6 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«a slow river of ice in the mountains» → ___", "(g…)", "glacier"),
 G("Planes produce more ___ per passenger than trains, so try to take the train for short trips.", "(e…)", "emissions"),
 D("«a colourless gas that plants use to grow and that is the main cause of global warming» → ___", "(c… d…)", "carbon dioxide"),
 G("Sunscreen is extra important in Australia and New Zealand, where the ___ above them is thinner.", "(o… l…)", "ozone layer"),
 D("«coal, oil and natural gas, which we burn to get energy» → ___", "(f… f…)", "fossil fuels"),
 G("Denmark gets more than half of its electricity from ___, mostly from wind farms in the North Sea.", "(r… e…)", "renewable energy"),
 G("There are now ___ on half the roofs in our street: they all point south.", "(s… p…)", "solar panels"),
 D("«a kind of animal, like the Sumatran tiger, with so few left that it risks disappearing» → ___", "(e… s…)", "endangered species"),
 G("Mammoths are ___, but some scientists want to bring them back with their DNA.", "(e…)", "extinct"),
 D("«to lower the total amount of CO2 that your lifestyle produces» → ___", "(r… y… c… f…)", "reduce your carbon footprint"),
 G("The supermarket's new «eco» water bottles are 99% plastic — that's just ___.", "(g…)", "greenwashing", ["greenwashing","green washing","green-washing"]),
 G("Instead of throwing away banana skins, Ada puts them on the ___ heap at the end of the garden.", "(c…)", "compost"),
 G("Tobia takes his bike to school all week to ___ the family's long drive to the mountains at the weekend.", "(m… u… f…)", "make up for"),
 G("— One flight a year is fine, the planet won't notice. — You're ___!", "(k… y…)", "kidding yourself"),
 G("In the far south of Morocco, people live on ___ land where palm trees grow only near the rivers.", "(a…)", "arid"),
 G("The ___ crossed the Pacific for a week before it hit Manila with winds of 200 kilometres an hour.", "(t…)", "typhoon"),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — No Planet B",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 G("Pompeii disappeared under metres of ash after the ___ of 79 AD.", "(v… e…)", "volcanic eruption"),
 D("«a fast flow of water over land that is normally dry, often after heavy rain» → ___", "(f…)", "flood", ["flood","flooding"]),
 G("Here the danger of ___ is high in summer: one cigarette in the dry grass can burn a whole hill.", "(w…)", "wildfires", ["wildfires","wildfire","wild fires"]),
 G("The ___ that hit Louisiana in 2005 destroyed thousands of homes and left New Orleans under water.", "(h…)", "hurricane"),
 G("Farmers in the Po Valley fear more summer ___ like the one in 2022, when the river dropped to its lowest level in seventy years.", "(d…)", "droughts"),
 G("Climbers must cross the ___ early in the morning, before the sun softens the ice and opens new cracks.", "(g…)", "glacier"),
 G("If the ice caps keep melting, ___ will rise and many coastal cities will be in danger.", "(s… l…)", "sea levels", ["sea levels","sea level"]),
 D("«a worldwide climate problem: each decade is a little hotter than the one before» → ___", "(g… w…)", "global warming"),
 G("Kenji worked out his ___ online: his two flights to Japan produce more CO2 than his car in a year.", "(c… f…)", "carbon footprint"),
 G("The village has had no rain for months, and the ___ that supplies its drinking water is almost empty.", "(r…)", "reservoir"),
 D("«a structure under the sea made by millions of tiny animals, home to many colourful fish» → ___", "(c… r…)", "coral reef"),
 G("Leave the radio on ___ if you like, but that little light still costs you money.", "(s…)", "standby", ["standby","stand-by"]),
 G("We pick the grapes by hand in late September, and the whole family comes to help in the ___.", "(v…)", "vineyard"),
 G("The snow leopard is still an ___: there are only a few thousand in the mountains of Asia.", "(e… s…)", "endangered species"),
 D("«frozen water on the tarmac, so thin and clear that drivers don't notice it» → ___", "(b… i…)", "black ice"),
 G("Our camping weekend ___: first the tent leaked, then the car didn't start.", "(verbo + from b… to w…)", "went from bad to worse"),
 G("By noon there was a nice ___ off the sea, and the sailing boats left the harbour.", "(b…)", "breeze"),
 G("Grandad collects rain in a ___ and uses it for his lemon trees.", "(w… b…)", "water butt"),
 G("— Is ___ really useful? — Planting trees helps, but flying less helps more.", "(c… o…)", "carbon offsetting", ["carbon offsetting","carbon offset"]),
 G("After a ___ December, with fourteen degrees at Christmas, the ski resorts opened late.", "(m…)", "mild"),
]))

# glossa: parole difficili delle definizioni e delle frasi + significato delle risposte
GLOSS = {
 "earthquake":"terremoto","shaking":"scossa, tremore","shook":"ha scosso","tsunami":"tsunami, maremoto","sirens":"sirene",
 "uphill":"in salita, verso l'alto","volcanic eruption":"eruzione vulcanica","ash":"cenere","landslide":"frana","landslip":"frana",
 "slides":"scivola","avalanche":"valanga","steep":"ripido","slope":"pendio","flood":"alluvione","flooding":"allagamento",
 "burst its banks":"è esondato","banks":"argini","wildfire":"incendio boschivo","wildfires":"incendi boschivi","hectares":"ettari",
 "pine":"pino","in flood":"in piena","planks":"assi","mud":"fango",
 "hurricane":"uragano","typhoon":"tifone","blizzard":"bufera di neve","snowstorm":"tempesta di neve","hail":"grandine",
 "hailstones":"chicchi di grandine","hailstorm":"grandinata","smashed":"ha distrutto, frantumato","walnuts":"noci",
 "lightning":"fulmine, fulmini","flash":"lampo","oak":"quercia","split":"ha spaccato","gale":"burrasca","gales":"burrasche",
 "droughts":"siccità (periodi di)","drought":"siccità","lorries":"camion","heatwave":"ondata di calore","shade":"ombra",
 "breeze":"brezza","mild":"mite","frost":"brina, gelata","frosts":"gelate","windscreen":"parabrezza","scrape":"raschiare",
 "arid":"arido","black ice":"ghiaccio sulla strada (invisibile)","bends":"curve","soaked":"fradicio","sodden":"zuppo",
 "sunburnt":"scottato dal sole","sunbed":"lettino","crunchy":"croccante, che scricchiola","lawn":"prato","hut":"rifugio",
 "tore":"ha strappato","poles":"paletti; poli","detour":"deviazione","swept away":"ha spazzato via","hillside":"pendio",
 "glacier":"ghiacciaio","ice caps":"calotte polari","sea level":"livello del mare","sea levels":"livello dei mari",
 "greenhouse effect":"effetto serra","carbon dioxide":"anidride carbonica","breathe out":"espirare","ozone layer":"strato di ozono",
 "ultraviolet rays":"raggi ultravioletti","emissions":"emissioni","fossil fuels":"combustibili fossili","coal":"carbone",
 "global warming":"riscaldamento globale","renewable energy":"energia rinnovabile","solar panels":"pannelli solari",
 "satellite":"satellite","jars":"barattoli","thermometer":"termometro","turbines":"turbine","boilers":"caldaie","barn":"fienile",
 "grid":"rete elettrica","power stations":"centrali elettriche","sunscreen":"crema solare",
 "endangered species":"specie in via di estinzione","extinct":"estinto","gorillas":"gorilla","dodo":"dodo","sailors":"marinai",
 "coral reef":"barriera corallina","reservoir":"bacino idrico","water shortage":"carenza d'acqua","water shortages":"carenze d'acqua",
 "wells":"pozzi","vineyard":"vigneto","grapes":"uva","harvest":"raccolto, vendemmia","crops":"raccolti, colture",
 "mammoths":"mammut","snow leopard":"leopardo delle nevi",
 "carbon footprint":"impronta di carbonio","carbon offsetting":"compensazione delle emissioni","greenwashing":"ecologismo di facciata",
 "pollutes":"inquina","compost":"compost","rots":"marcisce","peel":"buccia","coffee grounds":"fondi di caffè","heap":"mucchio",
 "reusable":"riutilizzabile","cloth":"stoffa","boot":"bagagliaio","checkout":"cassa","standby":"standby",
 "car-sharing":"car sharing","water butt":"cisterna per l'acqua piovana","make up for":"compensare",
 "go from bad to worse":"andare di male in peggio","went from bad to worse":"è andato di male in peggio",
 "kid yourself":"illuderti","kidding yourself":"ti illudi","straws":"cannucce","leaked":"faceva entrare acqua",
 "tarmac":"asfalto","snapped":"ha spezzato","skid":"slittare","colourless":"incolore","in a row":"di fila","chimneys":"camini","softens":"ammorbidisce","cracks":"crepacci","coastal":"costiero","supplies":"rifornisce",
}

# Schede di studio: [voce, definizione inglese, esempio nuovo, italiano] (+ True per i chunk da coprire interi)
STUDY = {
"1": [
 ["earthquake", "a sudden, violent shaking of the ground", "Japanese schools practise what to do in an earthquake.", "terremoto"],
 ["tsunami", "a huge sea wave, often produced by an earthquake under the ocean", "The tsunami of 2004 reached the coasts of Thailand and Sri Lanka.", "tsunami, maremoto"],
 ["volcanic eruption", "the moment when a mountain throws out hot rock, ash and gas", "Etna had a small volcanic eruption in May, and the airport in Catania closed for a day.", "eruzione vulcanica"],
 ["landslide", "a mass of earth and rocks that suddenly falls down the side of a hill", "The landslide left three houses on the edge of the cliff.", "frana"],
 ["avalanche", "a large amount of snow and ice that falls suddenly down a mountain", "Off-road skiers carry a special beeper in case of an avalanche.", "valanga"],
 ["flood", "a large amount of water that covers an area which is usually dry", "The flood of 1966 damaged thousands of old books in Florence.", "alluvione"],
 ["wildfire", "flames that spread quickly and out of control through forests or dry grass", "A wildfire can move faster than a person can run.", "incendio boschivo"],
 ["in flood", "(of a river) so full that the water goes over its banks", "In spring the Adige is often in flood after the snow melts.", "in piena"],
],
"2": [
 ["hurricane", "a violent storm with very strong winds that forms over the Atlantic Ocean", "The hurricane season in the Caribbean starts in June.", "uragano"],
 ["typhoon", "a violent tropical storm with very strong winds in the western Pacific", "A typhoon can bring a month's rain in a single day.", "tifone"],
 ["blizzard", "a snowstorm with strong winds, so you can see almost nothing", "We spent two days in the mountain hut because of a blizzard.", "bufera di neve"],
 ["hail", "small balls of ice that fall from the sky like rain", "Hail can dent cars and break windows in a few minutes.", "grandine"],
 ["lightning", "the sudden flash of bright light in the sky during a storm", "Count the seconds between the lightning and the thunder.", "fulmine, fulmini"],
 ["gale", "a very strong wind that blows for hours", "The gale blew the roof off our neighbour's shed.", "burrasca"],
 ["drought", "a long period with little or no rain", "During the drought, the town turned off the public fountains.", "siccità"],
 ["heatwave", "a period when the weather is much hotter than usual", "Old people should stay indoors in the afternoon during a heatwave.", "ondata di calore"],
],
"3": [
 ["breeze", "a light, pleasant wind", "A sea breeze makes the heat easier to bear.", "brezza"],
 ["mild", "(of weather, especially in winter) not too cold and quite pleasant", "The south of Italy usually has mild winters.", "mite"],
 ["frost", "a thin white layer of ice on grass and cars on very cold mornings", "Gardeners cover young plants to protect them from frost.", "brina, gelata"],
 ["arid", "so dry that almost no plants can grow there", "Camels can live for weeks in arid regions.", "arido"],
 ["black ice", "a dangerous, almost invisible frozen layer on the road in winter", "Black ice causes many accidents in the mountains in January.", "ghiaccio sulla strada (invisibile)"],
 ["soaked", "completely wet", "Take off those soaked trainers and borrow some dry socks.", "fradicio, bagnato fradicio"],
 ["sunburnt", "with red, painful skin after too much time in the sun", "Fair skin gets sunburnt in less than twenty minutes at noon.", "scottato dal sole"],
],
"4": [
 ["glacier", "a large mass of ice that moves very slowly down a mountain valley", "The Marmolada glacier is losing ice faster than ever.", "ghiacciaio"],
 ["ice caps", "the thick layers of ice near the North and South Poles", "When the ice caps melt, polar bears lose their hunting grounds.", "calotte polari"],
 ["sea level", "the average height of the sea", "Mount Everest is 8,849 metres above sea level.", "livello del mare"],
 ["greenhouse effect", "the warming of the Earth because gases in the air keep the sun's heat in", "Methane from cows adds to the greenhouse effect.", "effetto serra"],
 ["carbon dioxide", "the gas that we breathe out and that cars and factories produce (CO2)", "Forests store huge amounts of carbon dioxide.", "anidride carbonica"],
 ["ozone layer", "the part of the upper atmosphere that protects us from the sun's ultraviolet rays", "Some old fridge gases damaged the ozone layer.", "strato di ozono"],
 ["emissions", "gases like CO2 that cars, planes and factories send into the air", "Electric buses have no emissions from their exhaust pipes.", "emissioni"],
 ["burn fossil fuels", "fossil fuels: coal, oil and gas, formed from plants and animals that died millions of years ago", "Most cargo ships still burn fossil fuels, usually heavy oil.", "bruciare combustibili fossili"],
 ["global warming", "the slow rise in the average temperature of the Earth", "Global warming is changing the dates of the grape harvest in France.", "riscaldamento globale"],
 ["switch to renewable energy", "renewable energy: power from sources that never run out, like the sun, the wind and water", "Many farms switched to renewable energy after the price of gas went up.", "passare all'energia rinnovabile"],
 ["solar panels", "flat pieces of equipment on a roof that turn sunlight into electricity", "Solar panels work even on cloudy days, but less well.", "pannelli solari"],
],
"5": [
 ["endangered species", "a type of animal or plant that may soon disappear forever", "The Apennine brown bear is an endangered species.", "specie in via di estinzione"],
 ["extinct", "(of an animal or plant) with no members alive today", "Dinosaurs became extinct about 66 million years ago.", "estinto"],
 ["coral reef", "colourful rock-like structures under warm seas, built by tiny sea animals", "Snorkelling over a coral reef feels like swimming in an aquarium.", "barriera corallina"],
 ["reservoir", "an artificial lake that stores water for a town or for farms", "They built a dam across the valley to create a reservoir.", "bacino idrico"],
 ["water shortage", "a situation in which there is not enough water for everyone", "Cape Town had a terrible water shortage in 2018.", "carenza d'acqua"],
 ["vineyard", "a piece of land where grapes grow, usually to make wine", "We cycled through the vineyards of the Langhe in October.", "vigneto"],
 ["harvest", "the time when farmers collect their crops, or the crops that they collect", "The olive harvest in Puglia starts in November.", "raccolto; vendemmia"],
],
"6": [
 ["reduce your carbon footprint", "carbon footprint: the total amount of CO2 that a person or an activity produces", "You can reduce your carbon footprint by buying food from local farms.", "ridurre la propria impronta di carbonio"],
 ["carbon offsetting", "paying for projects, like planting trees, to balance the CO2 that you produce", "Critics say carbon offsetting lets rich people fly without guilt.", "compensazione delle emissioni"],
 ["greenwashing", "when a company pretends that its products are better for the environment than they really are", "A green leaf on a plastic bottle is a classic example of greenwashing.", "ecologismo di facciata"],
 ["compost", "a mix of dead leaves and food waste that rots and makes the soil rich", "Eggshells and tea bags are great for compost.", "compost"],
 ["reusable", "(of bags, cups or bottles) that you keep for a long time, not throw away after one go", "Take a reusable cup to the coffee machine at school.", "riutilizzabile"],
 ["standby", "the mode of a TV or computer that is off but still uses a little electricity", "Switch off the TV at the wall, not just on standby.", "standby"],
 ["car-sharing", "a service with cars that members can rent by the minute or by the hour", "Car-sharing is cheaper than owning a car if you drive only at weekends.", "car sharing"],
 ["water butt", "a large container in the garden that collects rain from the roof", "A water butt can save hundreds of litres of tap water in summer.", "cisterna per l'acqua piovana"],
 ["make up for", "to do something good so that a bad thing seems less bad", "An extra essay won't make up for three missing homework tasks.", "compensare"],
 ["go from bad to worse", "(of a bad situation) to become even more serious", "Without rain, things will go from bad to worse for the farmers.", "andare di male in peggio", True],
 ["kid yourself", "to believe something that is not true because you want to believe it", "Don't kid yourself: one cold winter doesn't mean the climate isn't changing.", "illudersi"],
],
}

CHUNK_HEADS = ("burn ","switch ","reduce ")
for _k in STUDY:
    STUDY[_k] = [r + [True] if r[0].startswith(CHUNK_HEADS) else r for r in STUDY[_k]]
