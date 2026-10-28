# Contenuti del lessico, Unit 7 "Get moving!"
from lexlib import *
UNIT = 7
NAME = "Get moving!"
TOPICS = "people in sport · places and equipment · matches and results · training and fitness · injuries"
META = "sport, fitness, matches, training and injuries"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — PEOPLE IN SPORT",
 desc="allenatori, arbitri, giocatori, tifosi · chi fa che cosa", rule=RULE, items=[
 D("«a person who trains a team or an athlete and decides how they should prepare» → ___", "(c…)", "coach"),
 D("«the official who controls a football match, blows the whistle and gives penalties» → ___", "(r…)", "referee"),
 D("«the player who stands in front of the net and tries to stop the ball with his or her hands» → ___", "(g…)", "goalkeeper", ["goalkeeper","goalie"]),
 D("«a player whose main job is to score goals, playing near the other team's goal» → ___", "(s…)", "striker"),
 D("«the leader of a team on the pitch, who often wears a band on his or her arm» → ___", "(c…)", "captain"),
 D("«a person or team that you play against in a game or competition» → ___", "(o…)", "opponent", ["opponent","opponents"]),
 D("«someone who plays in your own team» → ___", "(t…)", "teammate", ["teammate","teammates","team-mate","team-mates","team mate","team mates"]),
 D("«people who follow a team, go to its matches and sing for it» → ___", "(s…)", "supporters", ["supporters","supporter"]),
 D("«a person whose job is to watch the swimmers at a beach or pool and save them from danger» → ___", "(l…)", "lifeguard", ["lifeguard","lifeguards","life guard"]),
 D("«someone who has just started to learn a sport or an activity» → ___", "(b…)", "beginner", ["beginner","beginners"]),
 G("Our new ___ has changed the way we prepare for races: now we do two sessions on the track and one in the pool.", "(c…)", "coach"),
 G("The ___ blew the whistle three times and the players walked off the pitch.", "(r…)", "referee"),
 G("Our ___ dived to the left, but the ball went into the right corner of the net.", "(g…)", "goalkeeper", ["goalkeeper","goalie"]),
 G("Ferri plays up front: he's a ___, and his only job is to put the ball in the net.", "(s…)", "striker"),
 G("Giulia is the ___ of our volleyball team: she talks to the referee for all of us and leads the team on court.", "(c…)", "captain"),
 G("In the semi-final Marco played against an ___ much older than him and lost in three sets.", "(o…)", "opponent"),
 G("At the final whistle, Ugo ran to hug each of his ___ and then the coach.", "(t…)", "teammates", ["teammates","team-mates","team mates"]),
 G("Thousands of ___ in red and white shirts filled the trains to Turin for the away game.", "(s…)", "supporters", ["supporters","spectators"]),
 G("The ___ jumped down from his high chair and swam out to the child in trouble.", "(l…)", "lifeguard", ["lifeguard","life guard"]),
 G("This ski course is for complete ___: you don't need any experience at all.", "(b…)", "beginners"),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — PLACES AND EQUIPMENT",
 desc="campi e piste · l'attrezzatura: occhialini, cuffia, racchette, divisa", rule=RULE, items=[
 D("«the large area of grass where people play football or rugby» → ___", "(p…)", "pitch"),
 D("«the area with lines and a net where you play tennis or basketball» → ___", "(c…)", "court"),
 D("«an oval path, often 400 metres long, where athletes run races» → ___", "(t…)", "track"),
 D("«special glasses that protect your eyes underwater or in the snow» → ___", "(g…)", "goggles"),
 D("«a tight rubber hat that keeps your hair dry in the pool» → ___", "(s… c…)", "swimming cap", ["swimming cap","swim cap"]),
 D("«the object with a long handle and a net of strings that you use to hit the ball in tennis» → ___", "(r…)", "racket", ["racket","racquet"]),
 D("«things you wear on your hands to keep them warm or to protect them, for example in boxing» → ___", "(g…)", "gloves"),
 D("«shoes with studs underneath, which you wear on a grass pitch to play a match» → ___", "(f… b…)", "football boots"),
 D("«the shirt, shorts and socks of a team, all in the same colours» → ___", "(k…)", "kit"),
 D("«a gym machine with a moving belt, so you can run or walk without going anywhere» → ___", "(t…)", "treadmill"),
 G("It rained all night, so the ___ was too muddy for the match and the players trained indoors.", "(p…)", "pitch"),
 G("We booked the tennis ___ for six o'clock, but two old men were still playing on it.", "(c…)", "court"),
 G("The 400-metre runners lined up on the ___ and waited for the starting gun.", "(t…)", "track"),
 G("Without my ___, the chlorine in the pool makes my eyes red and sore.", "(g…)", "goggles"),
 G("At the public pool you must wear a ___ or the staff send you out of the water.", "(s… c…)", "swimming cap", ["swimming cap","swim cap"]),
 G("Mattia threw his ___ on the ground after the point and broke two strings.", "(r…)", "racket", ["racket","racquet"]),
 G("The boxers put on their ___ and touched them together before the fight.", "(g…)", "gloves"),
 G("Don't wear trainers on that wet grass: put on your ___ — the studs grip much better.", "(f… b…)", "football boots"),
 G("Our team has a new ___ this season: blue shirts with white shorts and socks.", "(k…)", "kit"),
 G("When it's icy outside, Rebecca runs on the ___ at the gym and watches the news on the little screen in front of her.", "(t…)", "treadmill"),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — persone, luoghi e attrezzatura dello sport",
 desc="i primi due livelli insieme · frasi e definizioni nuove", items=[
 D("«the person in charge of a team's training, who chooses the players for each match» → ___", "(c…)", "coach"),
 G("Nobody could score against their ___ that day: he stopped two penalties and a header.", "(g…)", "goalkeeper", ["goalkeeper","goalie"]),
 D("«a player at the front of the team, whose task is to put the ball in the net» → ___", "(s…)", "striker"),
 G("The ___ showed a red card to our defender after a terrible tackle.", "(r…)", "referee"),
 D("«a person on duty at a swimming pool or beach, ready to rescue people» → ___", "(l…)", "lifeguard", ["lifeguard","life guard"]),
 G("Put your ___ over your eyes before you dive, or the salt water will sting.", "(g…)", "goggles"),
 D("«what footballers put on their feet to avoid slipping on the grass» → ___", "(f… b…)", "football boots"),
 G("The tennis club has four clay ___ and two indoor ones.", "(c…)", "courts"),
 D("«a player on your own side in a game» → ___", "(t…)", "teammate", ["teammate","teammates","team-mate","team-mates","team mate","team mates"]),
 G("Our ___ wears the armband and tosses the coin with the referee before the match.", "(c…)", "captain"),
 D("«a running machine at the gym» → ___", "(t…)", "treadmill"),
 G("Two hours before the derby, the groundsman was still cutting the grass on the ___.", "(p…)", "pitch"),
 G("Don't worry if you fall off the board on your first day: we were all ___ once.", "(b…)", "beginners"),
 G("Lorenzo got a new ___ for his birthday: lighter, with a bigger head, perfect for his backhand.", "(r…)", "racket", ["racket","racquet"]),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — MATCHES AND RESULTS",
 desc="in trasferta, calcio d'inizio, rigori e parate · vincere, pareggiare, il campionato", rule=RULE, items=[
 D("«to play a match at the other team's stadium, not at home» → ___", "(p… a…)", "play away"),
 D("«the moment when a football match starts» → ___", "(k…)", "kick-off", ["kick-off","kick off","kickoff"]),
 D("«to shoot at goal from the spot, with only the goalkeeper in front of you» → ___", "(t… a p…)", "take a penalty"),
 D("«(of a goalkeeper) to stop a shot and keep the ball out of the net» → ___", "(m… a s…)", "make a save"),
 D("«the goal that decides a match and gives one team the victory» → ___", "(w… g…)", "winning goal"),
 D("«to finish with the same score for both teams» → ___", "(e… i… a d…)", "end in a draw"),
 D("«to defeat a person or a team in a game» → ___", "(b…)", "beat"),
 D("«a large number of people together in one place, for example at a match» → ___", "(c…)", "crowd"),
 D("«a group of teams that play against each other during the season to see which is the best» → ___", "(l…)", "league"),
 D("«to finish first in a championship and become the champions» → ___", "(w… t… t…)", "win the title"),
 D("«one after the other, without a break» → ___", "(i… a r…)", "in a row"),
 G("Next Sunday we ___ in Bari, so the bus leaves the school car park at seven for the long trip south.", "(verbo + a…)", "are playing away", ["are playing away","play away","'re playing away"]),
 G("The ___ is at three, so be at the stadium by half past two.", "(k…)", "kick-off", ["kick-off","kick off","kickoff"]),
 G("Our captain was too nervous to ___, so the young striker stepped up and scored.", "(verbo + a p…)", "take a penalty", ["take a penalty","take the penalty"]),
 G("In the ninetieth minute their goalkeeper ___ with his feet and kept the score at 0–0.", "(verbo + a s…)", "made a save"),
 G("Two minutes from the end, Diallo headed the ___ and the fans invaded the pitch.", "(w… g…)", "winning goal"),
 G("Neither team scored, so the match ___, nil–nil.", "(verbo + in a d…)", "ended in a draw", ["ended in a draw","finished in a draw"]),
 G("Tomorrow we play the champions. If we ___ them, we go top of the table.", "(b…)", "beat"),
 G("When Bianchi scored, the ___ jumped to its feet and the noise was incredible.", "(c…)", "crowd"),
 G("Our team finished third in the ___ this season, just two points behind the leaders.", "(l…)", "league"),
 G("Our town's team needs just one more point to ___: the whole town is ready to party.", "(verbo + the t…)", "win the title"),
 G("The Tigers have won five matches ___ — they haven't lost since October.", "(i… a r…)", "in a row"),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — TRAINING AND FITNESS",
 desc="riscaldamento e stretching · rimettersi in forma · gare, traguardi e cibo spazzatura", rule=RULE, items=[
 D("«to do gentle exercises before a sport so that your muscles get ready» → ___", "(w… u…)", "warm up", ["warm up","warm-up"]),
 D("«to pull your arms and legs long and hold the position, to make your muscles loose» → ___", "(s…)", "stretch"),
 D("«to do physical exercise, especially at a gym» → ___", "(w… o…)", "work out"),
 D("«to become healthy and strong through regular exercise» → ___", "(g… f…)", "get fit"),
 D("«a programme that tells you which exercises to do each day and for how long» → ___", "(t… p…)", "training plan", ["training plan","training programme","training program"]),
 D("«to go less fast» → ___", "(s… d…)", "slow down"),
 D("«to stop trying because something is too hard» → ___", "(g… u…)", "give up"),
 D("«food with lots of fat, salt or sugar and few vitamins, like crisps and burgers» → ___", "(j… f…)", "junk food"),
 D("«a sweet fizzy drink with lots of caffeine, sold in cans to give you a quick boost» → ___", "(e… d…)", "energy drink", ["energy drink","energy drinks"]),
 D("«extremely tired» → ___", "(e…)", "exhausted"),
 D("«to put your name down to take part in a competition for runners» → ___", "(e… a r…)", "enter a race"),
 D("«the line at the end of a race» → ___", "(f… l…)", "finish line", ["finish line","finishing line"]),
 G("Don't start sprinting straight away: ___ for ten minutes with some slow jogging first.", "(w… u…)", "warm up", ["warm up","warm-up"]),
 G("After the run, Pietro sits on the grass and ___ his legs to avoid stiffness the next day.", "(s…)", "stretches"),
 G("My sister ___ at the gym three evenings a week, mostly with weights.", "(w… o…)", "works out"),
 G("Dad wants to ___ before the summer, so he cycles to work and has stopped taking the lift.", "(g… f…)", "get fit"),
 G("The coach gave each runner a ___: twelve weeks of runs, rest days and gym sessions.", "(t… p…)", "training plan", ["training plan","training programme","training program"]),
 G("There's a sharp bend at the bottom of the hill, so ___ on your bike before you get there.", "(s… d…)", "slow down"),
 G("The climb was hard and Asia wanted to ___ halfway, but her friends cheered her on to the top.", "(g… u…)", "give up"),
 G("If you eat ___ before a match, you'll feel heavy and slow on the pitch.", "(j… f…)", "junk food"),
 G("Teenagers shouldn't have more than one ___ a day: they contain far too much caffeine.", "(e… d…)", "energy drink"),
 G("After the thirty-kilometre bike ride, Ivo was so ___ that he fell asleep on the sofa in his clothes.", "(e…)", "exhausted"),
 G("Sami filled in the online form and paid twenty euros to ___: a ten-kilometre run through the old town in April.", "(verbo + a r…)", "enter a race"),
 G("Hands in the air, Chloe crossed the ___ in first place.", "(f… l…)", "finish line", ["finish line","finishing line"]),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — INJURIES AND FAIR PLAY",
 desc="caviglie gonfie, strappi e infortuni · il fisioterapista · la correttezza sportiva", rule=RULE, items=[
 D("«the joint between your foot and your leg» → ___", "(a…)", "ankle"),
 D("«the joint in the middle of your leg, which bends when you sit down» → ___", "(k…)", "knee"),
 D("«bigger than normal, because of an injury or an infection» → ___", "(s…)", "swollen"),
 D("«to get hurt, for example during a sport» → ___", "(g… i…)", "get injured"),
 D("«to hurt one of the soft parts of your body that move your bones, by stretching it too much» → ___", "(p… a m…)", "pull a muscle"),
 D("«a person who treats injuries with exercises and massage» → ___", "(p…)", "physio", ["physio","physiotherapist"]),
 D("«playing honestly and respecting the rules and your opponents» → ___", "(f… p…)", "fair play"),
 G("Leo turned his ___ on the stairs and now he can't put his shoe on.", "(a…)", "ankle"),
 G("Marta fell off her bike and cut her ___: there's a big plaster just below her shorts.", "(k…)", "knee"),
 G("My wrist is twice its normal size: it's so ___ that I can't wear my watch.", "(s…)", "swollen"),
 G("Wear a helmet and protect your wrists — it's easy to ___ on a skateboard.", "(g… i…)", "get injured"),
 G("Gianni didn't warm up before the sprint and ___ in his leg.", "(verbo + a m…)", "pulled a muscle"),
 G("After the operation, Sara sees a ___ twice a week to get her leg strong again.", "(p…)", "physio", ["physio","physiotherapist"]),
 G("Both teams got a prize for ___: no yellow cards and lots of respect for the referee.", "(f… p…)", "fair play"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — partite, allenamento e infortuni",
 desc="livelli 3-5 e qualcosa di prima · frasi e definizioni nuove", items=[
 G("Next month we ___ in Palermo, a thousand kilometres from home.", "(verbo + a…)", "are playing away", ["are playing away","play away","'re playing away"]),
 D("«a competition in which each club plays all the others twice a season, home and away» → ___", "(l…)", "league"),
 G("Both goalkeepers were brilliant, and the derby ___: one goal each.", "(verbo + in a d…)", "ended in a draw", ["ended in a draw","finished in a draw"]),
 D("«to kick the ball at goal from the spot, with only the keeper to stop it» → ___", "(t… a p…)", "take a penalty"),
 G("The ___ sang and waved flags for ninety minutes, even in the rain.", "(c…)", "crowd"),
 G("Hundreds of people were waiting at the ___ with flags and bottles of water for the tired runners.", "(f… l…)", "finish line", ["finish line","finishing line"]),
 G("Never ___! You're only two kilometres from the end.", "(g… u…)", "give up"),
 D("«having no energy left at all» → ___", "(e…)", "exhausted"),
 G("To ___ properly, reach up high with both arms, hold for twenty seconds, then touch your toes.", "(s…)", "stretch"),
 G("I slipped on the wet floor of the changing room and twisted my ___; now I can't walk properly.", "(a…)", "ankle"),
 D("«to damage a muscle by stretching it too far» → ___", "(p… a m…)", "pull a muscle"),
 G("Esra ___ in the first ten minutes and spent the rest of the game on the bench with ice on her leg.", "(g… i…)", "got injured"),
 D("«the official in black who can show yellow and red cards» → ___", "(r…)", "referee"),
 G("The school canteen has stopped selling ___: no more burgers, chips or fizzy drinks.", "(j… f…)", "junk food"),
 D("«to win against someone» → ___", "(b…)", "beat"),
 G("Two weeks before the triathlon, Teo still can't swim well, so his coach has changed his ___.", "(t… p…)", "training plan", ["training plan","training programme","training program"]),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Get moving!",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 D("«the person who prepares the team and decides its tactics» → ___", "(c…)", "coach"),
 G("In the final seconds Rossi ___ — a dive to his right — and we kept a clean sheet.", "(verbo + a s…)", "made a save"),
 G("Zoe hit the ball so hard that it flew off the ___ and over the fence.", "(c…)", "court"),
 D("«the start of a football match, when one player kicks the ball from the centre» → ___", "(k…)", "kick-off", ["kick-off","kick off","kickoff"]),
 G("The two ___ shook hands and wished each other good luck before the final.", "(o…)", "opponents"),
 G("Fausto ___ in his thigh in the warm-up and missed the whole tournament.", "(verbo + a m…)", "pulled a muscle"),
 D("«the official clothes a team plays in» → ___", "(k…)", "kit"),
 G("Ricky hasn't missed a training session for months: he really wants to ___ before the season starts.", "(g… f…)", "get fit"),
 G("We won 2–1: Bea scored the ___ with a header in the ninetieth minute.", "(w… g…)", "winning goal"),
 D("«a person who is new to an activity and has little experience» → ___", "(b…)", "beginner", ["beginner","beginners"]),
 G("Mirko is a fast ___: give him the ball near the box and he'll score.", "(s…)", "striker"),
 D("«the grass area inside a stadium where the match takes place» → ___", "(p…)", "pitch"),
 G("The bee sting made her hand so ___ that she couldn't take her ring off.", "(s…)", "swollen"),
 G("After a perfect season, the girls' team ___ and lifted the cup in front of their fans.", "(verbo + the t…)", "won the title"),
 G("Our team has lost four games ___, and the coach is worried about his job.", "(i… a r…)", "in a row"),
 G("Long hair? Put it all under your ___ before you get in the water.", "(s… c…)", "swimming cap", ["swimming cap","swim cap"]),
 G("Wear shin pads, or you might ___ in a hard tackle.", "(g… i…)", "get injured"),
 G("The referee praised both teams for their ___: they helped each other up after each fall.", "(f… p…)", "fair play"),
 D("«someone who stands in front of the net and blocks shots» → ___", "(g…)", "goalkeeper", ["goalkeeper","goalie"]),
 G("Pamela spent an hour on the ___ in the hotel gym because it was pouring outside.", "(t…)", "treadmill"),
]))

# glossa: parole difficili delle definizioni e significato delle risposte
GLOSS = {
 "coach":"allenatore","athlete":"atleta","referee":"arbitro","whistle":"fischietto","blew the whistle":"fischiò",
 "penalties":"rigori","penalty":"rigore","goalkeeper":"portiere","goalie":"portiere","striker":"attaccante",
 "up front":"in attacco","captain":"capitano","armband":"fascia da capitano","tosses the coin":"lancia la monetina",
 "opponent":"avversario","opponents":"avversari","teammate":"compagno di squadra","teammates":"compagni di squadra",
 "supporters":"tifosi","lifeguard":"bagnino","beginner":"principiante","beginners":"principianti","on duty":"in servizio",
 "rescue":"soccorrere","sets":"set","semi-final":"semifinale",
 "pitch":"campo (da calcio)","muddy":"fangoso","court":"campo (da tennis, basket)","courts":"campi","clay":"terra rossa",
 "track":"pista","starting gun":"colpo di pistola della partenza","goggles":"occhialini","chlorine":"cloro",
 "sore":"irritati, doloranti","swimming cap":"cuffia","tight":"aderente","rubber":"gomma","racket":"racchetta",
 "handle":"manico","strings":"corde","gloves":"guanti","boxers":"pugili","football boots":"scarpe da calcio",
 "studs":"tacchetti","grip":"fare presa","kit":"divisa","treadmill":"tapis roulant","belt":"nastro",
 "sting":"bruciare; puntura","groundsman":"custode del campo","derby":"derby","backhand":"rovescio",
 "header":"colpo di testa","defender":"difensore","tackle":"contrasto, entrata",
 "play away":"giocare in trasferta","playing away":"giocare in trasferta","kick-off":"calcio d'inizio",
 "spot":"dischetto del rigore","save":"parata","made a save":"fece una parata","winning goal":"gol della vittoria",
 "headed":"colpì di testa","invaded":"invasero","draw":"pareggio","ended in a draw":"finì in pareggio",
 "nil–nil":"zero a zero","beat":"battere","defeat":"sconfiggere","top of the table":"in testa alla classifica",
 "crowd":"folla","league":"campionato","leaders":"capolista","title":"titolo","win the title":"vincere il campionato",
 "won the title":"vinse il campionato","in a row":"di fila","championship":"campionato","clean sheet":"porta inviolata",
 "warm up":"fare riscaldamento","warm-up":"riscaldamento","stretch":"fare stretching","stretches":"fa stretching",
 "loose":"sciolti","stiffness":"rigidità","work out":"allenarsi","works out":"si allena","get fit":"rimettersi in forma",
 "training plan":"programma di allenamento","rest days":"giorni di riposo","slow down":"rallentare","bend":"curva",
 "give up":"arrendersi","cheered her on":"la incoraggiarono","junk food":"cibo spazzatura","crisps":"patatine",
 "energy drink":"bevanda energetica","fizzy":"gassato","boost":"carica","exhausted":"sfinito",
 "enter a race":"iscriversi a una gara","put your name down":"iscriverti","finish line":"traguardo",
 "sprinting":"scattare, correre a tutta velocità","jogging":"corsa lenta","triathlon":"triathlon","canteen":"mensa",
 "ankle":"caviglia","knee":"ginocchio","joint":"articolazione","plaster":"cerotto","swollen":"gonfio",
 "wrist":"polso","wrists":"polsi","injured":"infortunato","get injured":"infortunarsi","got injured":"si infortunò",
 "pull a muscle":"farsi uno strappo","pulled a muscle":"si fece uno strappo","thigh":"coscia","physio":"fisioterapista",
 "massage":"massaggio","fair play":"correttezza sportiva","twisted":"storto","changing room":"spogliatoio",
 "bench":"panchina","shin pads":"parastinchi","praised":"lodò","bee sting":"puntura d'ape","tactics":"tattica",
 "pouring":"piove a dirotto","dived":"si tuffò","dive":"tuffo","skateboard":"skateboard",
}

# Schede di studio: [voce, definizione inglese, esempio nuovo, italiano] (+ True per i chunk da coprire interi)
STUDY = {
"1": [
 ["coach", "a person who trains a team or an athlete and decides how they should prepare", "The coach of our basketball team used to play for Italy.", "allenatore"],
 ["referee", "the official who controls a football match and gives penalties", "The referee stopped the game because a dog ran onto the grass.", "arbitro"],
 ["goalkeeper", "the player who stands in front of the net and tries to stop the ball", "Our goalkeeper is the shortest boy in the group, but he's very quick.", "portiere"],
 ["striker", "a player whose main job is to score goals", "That young striker is only seventeen, but the big clubs already want him.", "attaccante"],
 ["captain", "the leader of a team on the pitch", "The captain spoke to the players in the changing room.", "capitano"],
 ["opponent", "a person or team that you play against", "My opponent in the chess tournament was only nine years old.", "avversario"],
 ["teammate", "someone who plays in your own team", "My teammates threw me into the swimming pool to celebrate.", "compagno di squadra"],
 ["supporters", "people who follow a team and go to its matches", "The supporters waited outside the hotel to see the players.", "tifosi, sostenitori"],
 ["lifeguard", "a person whose job is to watch swimmers and save them from danger", "The lifeguard put up a red flag because of the big waves.", "bagnino"],
 ["beginner", "someone who has just started to learn a sport or an activity", "Surfing is hard for beginners: you fall off a hundred times.", "principiante"],
],
"2": [
 ["pitch", "the large area of grass where people play football or rugby", "Fans mustn't run onto the pitch.", "campo (da calcio, rugby)"],
 ["court", "the area with lines and a net where you play tennis or basketball", "There are two basketball courts behind our school.", "campo (da tennis, basket)"],
 ["track", "an oval path where athletes run races", "The athletics track at our stadium is bright blue.", "pista"],
 ["goggles", "special glasses that protect your eyes underwater or in the snow", "Skiers wear goggles to protect their eyes from the sun.", "occhialini, maschera"],
 ["swimming cap", "a tight rubber hat that keeps your hair dry in the pool", "My swimming cap is too small and it hurts my ears.", "cuffia"],
 ["racket", "the object with a handle and strings that you use in tennis", "Can I borrow your racket? I left mine at home.", "racchetta"],
 ["gloves", "things you wear on your hands to keep them warm or protect them", "In winter I go cycling in thick gloves.", "guanti"],
 ["football boots", "shoes with studs underneath that you wear on a grass pitch", "He cleans his football boots after each game.", "scarpe da calcio"],
 ["kit", "the shirt, shorts and socks of a team, all in the same colours", "This year the away kit is bright yellow.", "divisa"],
 ["treadmill", "a gym machine with a moving belt for running or walking", "I find running on a treadmill really boring.", "tapis roulant"],
],
"3": [
 ["play away", "to play a match at the other team's stadium", "We often lose when we play away.", "giocare in trasferta", True],
 ["kick-off", "the moment when a football match starts", "Kick-off is at eight, so let's eat before we go.", "calcio d'inizio"],
 ["take a penalty", "penalty: a free shot at goal from the spot, with only the goalkeeper to beat", "The referee gave a penalty after a handball.", "tirare un rigore"],
 ["make a save", "save: when a goalkeeper stops a shot and keeps the ball out of the net", "That was the best save of the tournament.", "fare una parata"],
 ["winning goal", "the goal that decides a match", "Who scored the winning goal in the cup final?", "gol della vittoria"],
 ["end in a draw", "draw: a result with the same score for both teams", "A draw is not a bad result away from home.", "finire in pareggio"],
 ["beat", "to defeat a person or a team in a game", "My little brother always beats me at ping-pong.", "battere, sconfiggere"],
 ["crowd", "a large number of people together in one place", "A huge crowd was waiting at the airport for the team.", "folla"],
 ["league", "a group of teams that play against each other during the season", "Our team is at the bottom of the league.", "campionato"],
 ["win the title", "title: the position of champion in a competition", "They lost the title on the final day of the season.", "vincere il campionato, il titolo"],
 ["in a row", "one after the other, without a break", "It has rained for five days in a row.", "di fila"],
],
"4": [
 ["warm up", "to do gentle exercises before a sport so that your muscles get ready", "We always warm up with a slow jog around the field.", "fare riscaldamento", True],
 ["stretch", "to pull your arms and legs long to loosen your muscles", "Cats stretch after they wake up.", "fare stretching, allungarsi"],
 ["work out", "to do physical exercise, especially at a gym", "She works out with a personal trainer.", "allenarsi", True],
 ["get fit", "to become healthy and strong through regular exercise", "Swimming is a great way to get fit.", "rimettersi in forma", True],
 ["training plan", "a programme that tells you which exercises to do each day", "My training plan includes two rest days a week.", "programma di allenamento"],
 ["slow down", "to go less fast", "Slow down! We're not in a hurry.", "rallentare", True],
 ["give up", "to stop trying because something is too hard", "Don't give up now — you're nearly there.", "arrendersi, rinunciare", True],
 ["junk food", "food with lots of fat, salt or sugar and few vitamins", "Athletes try to stay away from junk food.", "cibo spazzatura"],
 ["energy drink", "a sweet fizzy drink with lots of caffeine", "Energy drinks can keep you awake all night.", "bevanda energetica"],
 ["exhausted", "extremely tired", "I felt exhausted after the hike.", "sfinito"],
 ["enter a race", "to put your name down for a competition for runners", "At fifty, my dad decided to enter a race for the first time.", "iscriversi a una gara", True],
 ["finish line", "the line at the end of a race", "The finish line is in the main square.", "traguardo"],
],
"5": [
 ["ankle", "the joint between your foot and your leg", "I can't play tomorrow: my ankle still hurts.", "caviglia"],
 ["knee", "the joint in the middle of your leg", "Skiing is bad for my knees.", "ginocchio"],
 ["swollen", "bigger than normal because of an injury or an infection", "His eye was swollen after the boxing match.", "gonfio"],
 ["get injured", "to get hurt, for example during a sport", "Rugby players often get injured.", "infortunarsi", True],
 ["pull a muscle", "muscle: one of the soft parts of your body that move your bones", "You need strong muscles in your arms to climb.", "farsi uno strappo"],
 ["physio", "a person who treats injuries with exercises and massage", "The physio gave me some exercises for my back.", "fisioterapista"],
 ["fair play", "playing honestly and respecting the rules and your opponents", "Fair play means you don't pretend to fall.", "correttezza sportiva"],
],
}

# voci di base tolte nella revisione (decisione: niente lessico del primo/secondo anno)
_BASE = {"knee", "gloves", "slow down"}
for _L in LEVELS:
    _L["items"] = [it for it in _L["items"] if it[3].lower() not in _BASE]
for _k in STUDY:
    STUDY[_k] = [r for r in STUDY[_k] if r[0].lower() not in _BASE]
