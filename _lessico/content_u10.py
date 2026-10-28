# Contenuti del lessico, Unit 10 "Watch this space!"
from lexlib import *
UNIT = 10
NAME = "Watch this space!"
TOPICS = "TV programmes · watching and streaming · people on TV · news and social media · behind the scenes"
META = "TV programmes, streaming, people in the media, news and social media"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — TV PROGRAMMES",
 desc="soap, sitcom, quiz, talent, documentari · sigle", rule=RULE, items=[
 D("«a TV drama about the daily lives of the same group of characters, shown several times a week for years» → ___", "(s… o…)", "soap opera", ["soap opera","soap operas"]),
 D("«a funny series about the same characters, often at home or in an office, usually with recorded laughter» → ___", "(s…)", "sitcom"),
 D("«a TV competition in which contestants solve quizzes or puzzles for cash and prizes» → ___", "(g… s…)", "game show", ["game show","game shows"]),
 D("«a TV competition in which ordinary people sing, dance or perform, and a panel chooses the best» → ___", "(t… s…)", "talent show", ["talent show","talent shows"]),
 D("«a programme that follows a group of unknown people with cameras day and night, for example locked together in a villa» → ___", "(r… s…)", "reality show", ["reality show","reality shows"]),
 D("«a film or programme that gives facts about nature, history or science» → ___", "(d…)", "documentary"),
 D("«a report on TV or radio that says if the next days will be sunny, rainy or cold» → ___", "(w… f…)", "weather forecast"),
 D("«a TV show in which a chef prepares dishes and explains the recipes» → ___", "(c… p…)", "cookery programme", ["cookery programme","cooking programme","cookery program","cooking program"]),
 D("«one part of a TV series, broadcast on its own» → ___", "(e…)", "episode"),
 D("«the short piece of music at the start of a TV programme that everybody recognises» → ___", "(t… t…)", "theme tune"),
 G("My grandmother has followed the same Spanish ___ since 2009; she knows all the families in the fictional street and their secrets.", "(s… o…)", "soap opera"),
 G("The new ___ is set in a hotel reception, and the canned laughter after each joke drives me mad.", "(s…)", "sitcom"),
 G("My uncle went on a ___ and won a car by solving ten riddles about geography.", "(g… s…)", "game show"),
 G("Ten thousand people queued for the auditions of the new ___; only forty will perform in front of the panel.", "(t… s…)", "talent show"),
 G("Twelve strangers have to share a villa with cameras in all the rooms: it's the most popular ___ of the summer.", "(r… s…)", "reality show"),
 G("The ___ about Arctic whales took three years to film, and the underwater images are amazing.", "(d…)", "documentary"),
 G("Check the ___ before the hike: they're expecting thunderstorms in the afternoon.", "(w… f…)", "weather forecast"),
 G("Since she started watching that ___, Nina has tried all the chef's risotto recipes.", "(c… p…)", "cookery programme", ["cookery programme","cooking programme","cookery program","cooking program"]),
 G("Please, no spoilers: I still haven't watched the third ___ of the new season.", "(e…)", "episode"),
 G("When they hear the ___ of their favourite cartoon, my little cousins run to the sofa and start singing.", "(t… t…)", "theme tune"),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — WATCHING AND STREAMING",
 desc="telecomando, TV terrestre, abbonamenti · guardare in streaming · sottotitoli e pubblicità", rule=RULE, items=[
 D("«a small device with buttons that you use to change channel without getting up» → ___", "(r… c…)", "remote control"),
 D("«a TV station: you switch to a different one to see a different programme» → ___", "(c…)", "channel"),
 D("«normal TV that you receive with an aerial on the roof, not via satellite, cable or the internet» → ___", "(t… T…)", "terrestrial TV", ["terrestrial TV","terrestrial television"]),
 D("«a monthly payment that lets you watch films and series online» → ___", "(s… s…)", "streaming subscription"),
 D("«to watch or listen to something directly from the internet, without downloading it» → ___", "(s…)", "stream"),
 D("«to watch many episodes of a series one after another, in a single session» → ___", "(b…)", "binge-watch", ["binge-watch","binge watch","bingewatch"]),
 D("«the words of the dialogue written at the bottom of the screen, often translated» → ___", "(s…)", "subtitles"),
 D("«short films that try to sell you a product, shown between programmes» → ___", "(a…)", "adverts", ["adverts","ads","advertisements","advertising"]),
 D("«to save a programme so that you can watch it later» → ___", "(r…)", "record"),
 D("«broadcast at the same moment that it happens, not recorded before» → ___", "(l…)", "live"),
 D("«to make the sound of the TV or the radio quieter» → ___", "(t… d… t… v…)", "turn down the volume", ["turn down the volume","turn the volume down"]),
 G("Grandpa can never find the ___; it usually ends up between the sofa cushions.", "(r… c…)", "remote control"),
 G("This ___ shows nothing but old westerns and cooking competitions, day and night.", "(c…)", "channel"),
 G("The village is in a deep valley, so ___ doesn't work well and most families pay for satellite.", "(t… T…)", "terrestrial TV", ["terrestrial TV","terrestrial television"]),
 G("We share one ___ among four friends, so each of us pays three euros a month.", "(s… s…)", "streaming subscription"),
 G("Nobody in my family buys CDs: we ___ our music from apps, without downloading the songs.", "(s…)", "stream"),
 G("We ___ the whole second season on Saturday and didn't go to bed until four in the morning.", "(b…)", "binge-watched", ["binge-watched","binge watched","bingewatched"]),
 G("I watch Korean dramas in the original language with English ___ — it's good practice.", "(s…)", "subtitles"),
 G("The film lasts ninety minutes, but with all the ___ it takes almost two and a half hours.", "(a…)", "adverts", ["adverts","ads","advertisements"]),
 G("I'll be at training during the match, so could you ___ it for me?", "(r…)", "record"),
 G("The concert is ___ on the radio, so any wrong note goes straight out to the listeners.", "(l…)", "live"),
 G("I can't hear myself think! Could you ___ on that action film?", "(verbo + the v…)", "turn down the volume", ["turn down the volume","turn the volume down","lower the volume"]),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — programmi e modi di guardare la TV",
 desc="i primi due livelli insieme · frasi e definizioni nuove", items=[
 D("«a comedy series in which the same characters get into silly situations, episode after episode» → ___", "(s…)", "sitcom"),
 G("Mum cries at the end of nearly all the episodes of her favourite ___, the one about two rival families in a fishing village.", "(s… o…)", "soap opera"),
 G("On Saturday nights the whole family watches a ___ in which couples answer riddles to win a holiday.", "(g… s…)", "game show"),
 D("«a non-fiction film, for example about wild animals or a historical event» → ___", "(d…)", "documentary"),
 G("The ___ says it will snow on the hills tonight, so leave the car in the garage.", "(w… f…)", "weather forecast"),
 G("Who's got the ___? I want to switch to the football before the second half.", "(r… c…)", "remote control"),
 D("«to make a copy of a broadcast on your TV box for another day» → ___", "(r…)", "record"),
 G("Ilaria pays for two ___ — one for films and one for football — and she wants to cancel one.", "(s… s…)", "streaming subscriptions"),
 G("I can't understand the actors' Scottish accent without ___.", "(s…)", "subtitles"),
 G("Sorry, I'm a zombie today: I ___ six episodes of a medical drama in a row.", "(b…)", "binge-watched", ["binge-watched","binge watched","bingewatched"]),
 D("«the music that opens a series and helps people recognise it immediately» → ___", "(t… t…)", "theme tune"),
 G("The final of the singing competition is ___ on Saturday, so the public can vote by phone in real time.", "(l…)", "live"),
 G("There's a fifteen-minute break for ___ in the middle of the film, so go and make some popcorn.", "(a…)", "adverts", ["adverts","ads","advertisements"]),
 D("«a programme that films unknown people day and night in a house or on an island» → ___", "(r… s…)", "reality show"),
 G("Each ___ of this crime series lasts fifty minutes, and there are ten in the season.", "(e…)", "episode"),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — PEOPLE ON TV",
 desc="chi conduce, chi gareggia, chi giudica · chi produce · chi fa video online", rule=RULE, items=[
 D("«the person who introduces a TV or radio programme and talks to the guests» → ___", "(p…)", "presenter"),
 D("«the person who leads a TV show and welcomes the guests, especially a chat show» → ___", "(h…)", "host"),
 D("«the person who reads the news on TV or radio» → ___", "(n…)", "newsreader", ["newsreader","newscaster"]),
 D("«a person who takes part in a competition or a quiz on TV» → ___", "(c…)", "contestant", ["contestant","competitor"]),
 D("«the people who decide who is the best in a competition» → ___", "(j…)", "judges"),
 D("«the people who watch or listen to a show, in the studio or at home» → ___", "(a…)", "audience"),
 D("«the person who controls the money and the organisation of a film or programme» → ___", "(p…)", "producer"),
 D("«the person who tells the actors what to do and decides how a film is shot» → ___", "(d…)", "director"),
 D("«a person who regularly posts videos about their life or interests online» → ___", "(v…)", "vlogger"),
 G("The ___ of the quiz read the question again, and the studio went silent.", "(p…)", "presenter"),
 G("Everybody loves the ___ of the late-night chat show: his jokes about politicians are famous.", "(h…)", "host"),
 G("At eight o'clock sharp the ___ appeared on screen with the day's main stories.", "(n…)", "newsreader", ["newsreader","newscaster"]),
 G("The youngest ___ got all twelve questions right and took home fifty thousand euros.", "(c…)", "contestant", ["contestant","competitor"]),
 G("After her song, all four ___ stood up and clapped.", "(j…)", "judges"),
 G("The studio ___ laughed so loudly that the actors had to wait before the next line.", "(a…)", "audience"),
 G("The ___ decided to cut the show to thirty minutes because it was too expensive.", "(p…)", "producer"),
 G("The ___ made the actors repeat the kiss scene fourteen times before she was happy.", "(d…)", "director"),
 G("Mattia is a travel ___: he films his trips and puts a new clip on his channel twice a week.", "(v…)", "vlogger"),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — NEWS AND SOCIAL MEDIA",
 desc="bacheca, follower, newsletter, chat di gruppo · conferenze stampa e scandali", rule=RULE, items=[
 D("«the list of recent posts and news that you see when you open a social media app» → ___", "(n…)", "newsfeed", ["newsfeed","news feed"]),
 D("«the people who see your posts because they have chosen to get your updates» → ___", "(f…)", "followers"),
 D("«a regular email with news from a company, a club or a website» → ___", "(n…)", "newsletter"),
 D("«a conversation in a messaging app with several people at the same time» → ___", "(g… c…)", "group chat"),
 D("«a meeting where an important person answers journalists' questions» → ___", "(p… c…)", "press conference"),
 D("«an event that shocks people because someone important has done something wrong» → ___", "(s…)", "scandal"),
 D("«a programme sent out on TV or radio» → ___", "(b…)", "broadcast"),
 D("«the folder where new emails arrive» → ___", "(i…)", "inbox"),
 G("I scrolled through my ___ on the bus and saw the photos of Elisa's party.", "(n…)", "newsfeed", ["newsfeed","news feed"]),
 G("Her cooking account has over two hundred thousand ___.", "(f…)", "followers"),
 G("Sign up for the museum's ___ and you'll get news about the exhibitions each month.", "(n…)", "newsletter"),
 G("The class ___ was full of voice messages until our teacher joined it.", "(g… c…)", "group chat"),
 G("The mayor is going to ___ at noon to present the new bike lanes.", "(verbo + a p… c…)", "hold a press conference", ["hold a press conference","give a press conference","call a press conference"]),
 G("The ___ about the minister's secret bank accounts was on all the front pages.", "(s…)", "scandal"),
 G("The ___ of the royal wedding reached three hundred million people around the world.", "(b…)", "broadcast"),
 G("After the holidays my ___ had four hundred unread emails.", "(i…)", "inbox"),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — BEHIND THE SCENES",
 desc="studio, prove, provini · dietro le quinte · in onda, montaggio, premi e autografi", rule=RULE, items=[
 D("«a room where TV programmes, music or films are recorded» → ___", "(s…)", "studio"),
 D("«a practice of a show or a play before the real performance» → ___", "(r…)", "rehearsal"),
 D("«a short performance to show if you are good enough for a part in a show» → ___", "(a…)", "audition"),
 D("«in the area behind the stage, where the performers get ready» → ___", "(b…)", "backstage"),
 D("«being broadcast at this moment on radio or TV» → ___", "(o… a…)", "on air"),
 D("«to choose, cut and put in order the parts of a film or video» → ___", "(e…)", "edit"),
 D("«the cash that the winner of a competition receives» → ___", "(p… m…)", "prize money"),
 D("«a famous person's signature, which fans collect» → ___", "(a…)", "autograph"),
 G("The quiz is recorded in a ___ outside Rome, with two hundred seats for the public.", "(s…)", "studio"),
 G("The dancers were exhausted after a six-hour ___, and the show was the following evening.", "(r…)", "rehearsal"),
 G("Three hundred young singers came to the ___, but only ten got a place in the musical.", "(a…)", "audition"),
 G("After the concert, a security guard took us ___ to meet the band.", "(b…)", "backstage"),
 G("Turn off your phones, please: we go ___ in thirty seconds.", "(o… a…)", "on air"),
 G("It takes Kevin a whole weekend to ___ each ten-minute video for his channel.", "(e…)", "edit"),
 G("The winner of the baking contest will use the ___ to open her own pastry shop.", "(p… m…)", "prize money"),
 G("I've got a photo with the singer and her ___ on the back of my concert ticket.", "(a…)", "autograph"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — persone, notizie, dietro le quinte",
 desc="livelli 3-5 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«the person in charge of a chat show, who chats with the famous guests on the sofa» → ___", "(h…)", "host"),
 G("The ___ fell off her chair when she heard that the car was hers.", "(c…)", "contestant", ["contestant","competitor"]),
 G("The ___ shouted «Cut!» and the actors stopped in the middle of the scene.", "(d…)", "director"),
 D("«someone who films short clips about their daily life and shares them on the web» → ___", "(v…)", "vlogger"),
 G("The ___ at home can vote for their favourite singer by text message.", "(a…)", "audience"),
 G("My cousin works for a local channel: she's the youngest ___ in the region and presents the evening bulletin.", "(n…)", "newsreader", ["newsreader","newscaster"]),
 D("«a list of updates and posts on the screen of a social app» → ___", "(n…)", "newsfeed", ["newsfeed","news feed"]),
 G("In one week the cat video brought him fifty thousand new ___.", "(f…)", "followers"),
 G("The singer's private jet trips caused a huge ___, and three sponsors dropped her.", "(s…)", "scandal"),
 G("Tomorrow the club president will ___ to introduce the new coach to the journalists.", "(verbo + a p… c…)", "hold a press conference", ["hold a press conference","give a press conference","call a press conference"]),
 D("«the part of your email account that holds the messages sent to you» → ___", "(i…)", "inbox"),
 G("The actors had their final ___ in costume on Friday, the day before the première.", "(r…)", "rehearsal"),
 G("The sound engineer is still checking the microphones, and we're ___ in two minutes!", "(o… a…)", "on air"),
 G("With a special pass, the winners of the radio contest went ___ and watched the dancers put on their make-up.", "(b…)", "backstage"),
 G("She spent the ___ on a new laptop and a trip to Lisbon.", "(p… m…)", "prize money"),
 D("«a test performance for actors, singers or dancers who want a role» → ___", "(a…)", "audition"),
 G("The famous chef wrote his ___ on my cookbook, with a little drawing of a lemon.", "(a…)", "autograph"),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Watch this space!",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 D("«a light comedy on TV about a family, a group of friends or colleagues» → ___", "(s…)", "sitcom"),
 G("I can't stand the ___ in the middle of films; that's why I pay for streaming.", "(a…)", "adverts", ["adverts","ads","advertisements"]),
 G("Pietro and Giulia ___ all eight episodes of the Danish thriller in one weekend.", "(b…)", "binge-watched", ["binge-watched","binge watched","bingewatched"]),
 G("Our holiday flat has only ___: an old aerial on the roof, a few local stations and no internet.", "(t… T…)", "terrestrial TV", ["terrestrial TV","terrestrial television"]),
 D("«a person who has to answer questions or complete tasks in a TV competition» → ___", "(c…)", "contestant", ["contestant","competitor"]),
 G("The four ___ gave her a perfect score, and the crowd went wild.", "(j…)", "judges"),
 D("«the man or woman in charge of a film, who guides the actors» → ___", "(d…)", "director"),
 G("Our school sends a ___ to all parents on the first Monday of the month.", "(n…)", "newsletter"),
 G("My aunts created a family ___, and now they send good-morning photos at six a.m.", "(g… c…)", "group chat"),
 G("The radio station had to stop its ___ for ten minutes because of a power cut.", "(b…)", "broadcast"),
 G("Your sister is doing her homework next door, so please ___ a bit.", "(verbo + the v…)", "turn down the volume", ["turn down the volume","turn the volume down","lower the volume"]),
 G("Before the première, the cast had three ___ a day for a whole week.", "(r…)", "rehearsals"),
 G("Marta practised her monologue for weeks before the ___ for a part in a TV series.", "(a…)", "audition"),
 D("«the room where a TV show is filmed, with cameras, lights and a set» → ___", "(s…)", "studio"),
 G("After the fake giveaway, the influencer lost thousands of ___.", "(f…)", "followers"),
 G("The questions were hard, but the ___ was huge: a hundred thousand euros.", "(p… m…)", "prize money"),
 G("I always ___ the late film and watch it the next afternoon.", "(r…)", "record"),
 D("«lines of text under the pictures of a film, for people who don't know the language or can't hear well» → ___", "(s…)", "subtitles"),
 G("There are over two hundred ___ on our satellite TV, and there's still nothing to watch!", "(c…)", "channels"),
]))

GLOSS = {
 "soap opera":"soap opera, telenovela","soap operas":"soap opera","sitcom":"sitcom, commedia a episodi",
 "game show":"quiz televisivo","talent show":"talent show","reality show":"reality show","documentary":"documentario",
 "weather forecast":"previsioni del tempo","cookery programme":"programma di cucina","cooking programme":"programma di cucina",
 "episode":"puntata, episodio","episodes":"puntate","theme tune":"sigla","season":"stagione",
 "remote control":"telecomando","channel":"canale","terrestrial TV":"TV terrestre","aerial":"antenna",
 "satellite dish":"parabola","streaming subscription":"abbonamento a una piattaforma di streaming",
 "streaming subscriptions":"abbonamenti streaming","stream":"guardare in streaming","binge-watch":"guardare tutto di fila",
 "binge-watched":"ha/hanno guardato tutto di fila","subtitles":"sottotitoli","adverts":"pubblicità","record":"registrare",
 "live":"in diretta","turn down the volume":"abbassare il volume","volume":"volume",
 "presenter":"conduttore, conduttrice","host":"conduttore, padrone di casa","newsreader":"conduttore del telegiornale",
 "contestant":"concorrente","judges":"giudici","panel":"giuria","audience":"pubblico","producer":"produttore",
 "director":"regista","vlogger":"vlogger, videoblogger","chat show":"talk show",
 "newsfeed":"bacheca delle notizie","followers":"follower","newsletter":"newsletter","group chat":"chat di gruppo",
 "press conference":"conferenza stampa","hold a press conference":"tenere una conferenza stampa","scandal":"scandalo",
 "broadcast":"trasmissione","broadcasting":"trasmissione","inbox":"casella di posta in arrivo",
 "studio":"studio televisivo","rehearsal":"prova","rehearsals":"prove","audition":"provino","auditions":"provini",
 "backstage":"dietro le quinte","on air":"in onda","edit":"montare (un video)","prize money":"premio in denaro",
 "autograph":"autografo","signature":"firma",
 "canned laughter":"risate registrate","riddles":"indovinelli","queued":"hanno fatto la fila","strangers":"sconosciuti",
 "locked":"chiusi dentro","whales":"balene","underwater":"subacquee","thunderstorms":"temporali","hike":"escursione",
 "spoilers":"anticipazioni","cushions":"cuscini","westerns":"film western","valley":"valle","downloading":"scaricare",
 "straight":"direttamente","wrong note":"nota stonata","rival":"rivali","non-fiction":"basato su fatti reali",
 "switch":"passare (a un canale)","zombie":"zombie","accent":"accento","popcorn":"popcorn","sharp":"in punto","monologue":"monologo","power cut":"blackout","make-up":"trucco","in a row":"di fila","channels":"canali",
 "clapped":"hanno applaudito","shot":"girato","clip":"video breve","clips":"video brevi","scrolled":"ho fatto scorrere",
 "sign up":"iscriviti","unread":"non letti","front pages":"prime pagine","royal":"reale",
 "exhausted":"sfiniti","pastry shop":"pasticceria","security guard":"guardia di sicurezza","bulletin":"notiziario",
 "sponsors":"sponsor","dropped":"hanno scaricato, abbandonato","première":"prima (di uno spettacolo)",
 "sound engineer":"tecnico del suono","pass":"pass, permesso","cast":"cast, attori","giveaway":"concorso a premi online",
 "derby":"derby","crowd":"folla, pubblico","performers":"artisti","performance":"esibizione","costume":"costume di scena",
}

STUDY = {
"1": [
 ["soap opera", "a TV drama about the daily lives of the same group of characters, shown for years", "That soap opera started before I was born, and it's still on.", "soap opera"],
 ["sitcom", "a funny series about the same characters, usually with recorded laughter", "Which sitcom do you watch with your parents?", "sitcom, commedia a episodi"],
 ["game show", "a TV competition in which contestants solve quizzes or puzzles for cash and prizes", "Grandad shouts the answers at the game show from his armchair.", "quiz televisivo"],
 ["talent show", "a TV competition in which ordinary people sing, dance or perform", "A boy from my village reached the final of a talent show.", "talent show"],
 ["reality show", "a programme that follows a group of unknown people with cameras day and night", "Would you ever take part in a reality show on a desert island?", "reality show"],
 ["documentary", "a film or programme that gives facts about nature, history or science", "Our science teacher showed us a documentary on volcanoes.", "documentario"],
 ["weather forecast", "a report that says if the next days will be sunny, rainy or cold", "Fishermen listen carefully to the weather forecast before going out.", "previsioni del tempo"],
 ["cookery programme", "a TV show in which a chef prepares dishes and explains the recipes", "My dad learnt to make sushi from a cookery programme.", "programma di cucina"],
 ["episode", "one part of a TV series, broadcast on its own", "The pilot episode was boring, but the series gets better.", "puntata, episodio"],
 ["theme tune", "the short piece of music at the start of a TV programme", "I can't get that theme tune out of my head.", "sigla"],
],
"2": [
 ["remote control", "a small device with buttons that you use to change channel", "The dog chewed the remote control, so now the buttons don't work.", "telecomando"],
 ["channel", "a TV station that you switch to for a different programme", "Is there a channel with only sport on it?", "canale"],
 ["terrestrial TV", "normal TV that you receive with an aerial, not via satellite, cable or the internet", "In the mountain hut there's only terrestrial TV, with five fuzzy stations.", "TV terrestre"],
 ["streaming subscription", "subscription: a regular payment for a service, like films and series online", "My subscription costs less if I pay for the whole year.", "abbonamento streaming"],
 ["stream", "to watch or listen to something directly from the internet", "You can stream the match on your tablet if the TV is busy.", "guardare in streaming"],
 ["binge-watch", "to watch many episodes of a series one after another", "Don't binge-watch the night before an exam!", "guardare tutto di fila"],
 ["subtitles", "the words of the dialogue written at the bottom of the screen", "Switch on the subtitles: Grandma is a bit deaf.", "sottotitoli"],
 ["advert", "a short film that tries to sell you a product", "That advert for crisps is funnier than the programme.", "pubblicità, spot"],
 ["record", "to save a programme so that you can watch it later", "Our old TV box can record two programmes at once.", "registrare"],
 ["live", "broadcast at the same moment that it happens", "The prime minister's speech is live at nine.", "in diretta"],
 ["turn down the volume", "volume: how loud a sound is", "Dad always turns down the volume during the adverts.", "abbassare il volume", True],
],
"3": [
 ["presenter", "the person who introduces a programme and talks to the guests", "The presenter of the breakfast show gets up at three a.m.", "conduttore, conduttrice"],
 ["host", "the person who leads a TV show and welcomes the guests", "The host forgot the name of his guest and turned red.", "conduttore, padrone di casa"],
 ["newsreader", "the person who reads the news on TV or radio", "A newsreader has to stay calm, even with terrible stories.", "conduttore del telegiornale"],
 ["contestant", "a person who takes part in a competition or a quiz on TV", "One contestant forgot the words of her song.", "concorrente"],
 ["judge", "a person who decides who is the best in a competition", "The strictest judge never smiles.", "giudice"],
 ["audience", "the people who watch or listen to a show", "The audience booed the referee's decision.", "pubblico"],
 ["producer", "the person who controls the money and the organisation of a film or programme", "A good producer finds the money for the project.", "produttore"],
 ["director", "the person who tells the actors what to do and decides how a film is shot", "Who's the director of that horror film with the clown?", "regista"],
 ["vlogger", "a person who regularly posts videos about their life or interests", "My neighbour is a gaming vlogger with a huge fan base.", "vlogger, videoblogger"],
],
"4": [
 ["newsfeed", "the list of recent posts and news that you see in a social media app", "My newsfeed is full of holiday pictures in August.", "bacheca delle notizie"],
 ["followers", "the people who see your posts because they have chosen to get your updates", "Buying fake followers is against the rules of most apps.", "follower"],
 ["newsletter", "a regular email with news from a company, a club or a website", "The gym newsletter announced two new yoga classes.", "newsletter"],
 ["group chat", "a conversation in a messaging app with several people", "Please mute the group chat during the lesson.", "chat di gruppo"],
 ["hold a press conference", "press conference: a meeting where an important person answers journalists' questions", "After a big arrest, the police chief usually holds a press conference.", "tenere una conferenza stampa", True],
 ["scandal", "an event that shocks people because someone important has done something wrong", "The doping scandal ended his career.", "scandalo"],
 ["broadcast", "a programme sent out on TV or radio", "The first radio broadcast in Italy was in 1924.", "trasmissione"],
 ["inbox", "the folder where new emails arrive", "Check your inbox: the tickets should be there.", "casella di posta in arrivo"],
],
"5": [
 ["studio", "a room where TV programmes, music or films are recorded", "The band rented a studio for a week to make their album.", "studio (televisivo, di registrazione)"],
 ["rehearsal", "a practice of a show or a play before the real performance", "The dress rehearsal went badly, but the opening night was perfect.", "prova"],
 ["audition", "a short performance to show if you are good enough for a part in a show", "Leo was so nervous at the audition that his hands shook.", "provino"],
 ["backstage", "in the area behind the stage, where the performers get ready", "Backstage, the actors were changing costumes in a hurry.", "dietro le quinte"],
 ["on air", "being broadcast at this moment on radio or TV", "When the red light is on, the DJ is on air.", "in onda"],
 ["edit", "to choose, cut and put in order the parts of a film or video", "Learning to edit with free software is easy.", "montare (un video)"],
 ["prize money", "the cash that the winner of a competition receives", "The tournament's prize money goes to charity.", "premio in denaro"],
 ["autograph", "a famous person's signature, which fans collect", "The goalkeeper stopped to give an autograph to a little girl.", "autografo"],
],
}

# voci di base tolte nella revisione (decisione: niente lessico del primo/secondo anno)
_BASE = {"record", "live", "channel", "channels", "episode", "audience", "director"}
for _L in LEVELS:
    _L["items"] = [it for it in _L["items"] if it[3].lower() not in _BASE]
for _k in STUDY:
    STUDY[_k] = [r for r in STUDY[_k] if r[0].lower() not in _BASE]
