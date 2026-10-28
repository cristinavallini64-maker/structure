# Contenuti del lessico, Unit 8 "Crime and punishment"
from lexlib import *
UNIT = 8
NAME = "Crime and punishment"
TOPICS = "criminals and crimes · investigation and evidence · in court · punishment · definizioni e collocazioni"
META = "criminals, crimes, investigation, evidence, courts and punishment"
SK_VER = ""
RULE = RULE_STD
LEVELS = []

# ---------------------------------------------------------------- 01
LEVELS.append(dict(id=1, type="study", title="LIVELLO 01 — CRIMINALS",
 desc="ladri, rapinatori, truffatori, vandali e complici", rule=RULE, items=[
 D("«a person who gets into a house or a flat, usually at night, to take things» → ___", "(b…)", "burglar"),
 D("«a criminal who goes into a bank, often with a gun, and takes the money» → ___", "(b… r…)", "bank robber"),
 D("«a thief who quietly takes wallets and phones from people's bags and clothes in crowded places» → ___", "(p…)", "pickpocket"),
 D("«someone who takes things from a shop without paying for them» → ___", "(s…)", "shoplifter"),
 D("«a person who tricks people, often online or by phone, to get their money» → ___", "(f…)", "fraudster"),
 D("«people who break or damage things in public places, such as bus shelters or park benches, just for fun» → ___", "(v…)", "vandals", ["vandals","vandal"]),
 D("«someone who gets into other people's computers or online accounts without permission» → ___", "(h…)", "hacker"),
 D("«a person who helps someone else to commit a crime» → ___", "(a…)", "accomplice"),
 G("The Ferraris came back from their holiday to find the back door forced and the drawers empty: a ___ had got in during the night.", "(b…)", "burglar"),
 G("The ___ wore a clown mask and escaped with forty thousand euros from the cashier's desk.", "(b… r…)", "bank robber"),
 G("Hold your bag in front of you on the metro: there's often a ___ among the tourists at rush hour.", "(p…)", "pickpocket"),
 G("Our local supermarket has a new problem: a ___ who walks out with chocolate and razors in her coat pockets twice a week.", "(s…)", "shoplifter"),
 G("The email looked like a message from my bank, but it came from a ___ who wanted my PIN.", "(f…)", "fraudster"),
 G("During the night ___ broke all the lights in the park and covered the benches with spray paint.", "(v…)", "vandals"),
 G("A sixteen-year-old ___ got into the school's computer system and changed his own marks.", "(h…)", "hacker"),
 G("The burglar didn't work alone: his ___ waited outside in the car with the engine running.", "(a…)", "accomplice"),
]))

# ---------------------------------------------------------------- 02
LEVELS.append(dict(id=2, type="study", title="LIVELLO 02 — CRIMES AND BREAK-INS",
 desc="furti, rapine e truffe · entrare con la forza · dare fuoco · apposta", rule=RULE, items=[
 D("«the crime of getting into a building to take things» → ___", "(b…)", "burglary"),
 D("«the crime of taking money or things from a person or a place, often with violence or threats» → ___", "(r…)", "robbery"),
 D("«the crime of tricking people to get money from them» → ___", "(f…)", "fraud"),
 D("«to enter a building or a car illegally, often by damaging a door or a window» → ___", "(b… i…)", "break into", ["break into","break in"]),
 D("«an occasion when someone enters a building illegally to take something» → ___", "(b…-i…)", "break-in", ["break-in","break in"]),
 D("«to make something start burning, usually on purpose» → ___", "(s… f… t…)", "set fire to"),
 D("«not by accident; because you really wanted to do it» → ___", "(o… p…)", "on purpose"),
 D("«a crime that someone plans or commits from inside the place where they work» → ___", "(i… j…)", "inside job"),
 G("There were three cases of ___ in our street in October, so now everyone locks the gate at night.", "(b…)", "burglary", ["burglary","burglaries"]),
 G("Two men in masks took all the cash from the post office this morning: it's the third armed ___ in the area this year.", "(r…)", "robbery"),
 G("Selling fake concert tickets online is a kind of ___, and you can go to prison for it.", "(f…)", "fraud"),
 G("Someone tried to ___ our car: they smashed the side window, but the alarm went off.", "(b… i…)", "break into"),
 G("After the ___ at the pharmacy, the owner put metal bars on all the windows.", "(b…-i…)", "break-in", ["break-in","break in"]),
 G("Some teenagers ___ the rubbish bins behind the gym, and the neighbours called the emergency services.", "(verbo + f… t…)", "set fire to"),
 G("Tommaso says he broke the window by mistake, but the neighbour saw him throw the stone ___.", "(o… p…)", "on purpose"),
 G("Nobody forced the doors and the alarm stayed silent, so the manager suspects an ___ by one of her own employees.", "(i… j…)", "inside job"),
]))

# ---------------------------------------------------------------- 03
LEVELS.append(dict(id=3, type="study", title="LIVELLO 03 — THE INVESTIGATION",
 desc="sospettati, testimoni, alibi, moventi e indizi · risolvere il caso", rule=RULE, items=[
 D("«a person who the police think may be guilty of a crime» → ___", "(s…)", "suspect"),
 D("«someone who sees a crime or an accident and can describe what happened» → ___", "(w…)", "witness"),
 D("«proof that you were in a different place when a crime happened» → ___", "(a…)", "alibi"),
 D("«the reason why someone commits a crime» → ___", "(m…)", "motive"),
 D("«a small piece of information or an object that helps to find the answer to a mystery» → ___", "(c…)", "clue"),
 D("«a name that is not your real one, which you use to hide who you are» → ___", "(f… n…)", "fake name", ["fake name","false name"]),
 D("«to find out who committed a crime and how» → ___", "(s… t… c…)", "solve the case", ["solve the case","solve a case"]),
 D("«a person who suffers because of a crime» → ___", "(v…)", "victim"),
 G("The police have only one ___ for the robbery at the petrol station: a man with a red scooter.", "(s…)", "suspect"),
 G("The only ___ to the hit-and-run was a boy on a bike: he saw the car and remembered half the number plate.", "(w…)", "witness"),
 G("Marco has a good ___: at the time of the robbery he was at the dentist's, and the receptionist remembers him.", "(a…)", "alibi"),
 G("Why would the old gardener want to hurt his boss? The detectives still can't find a ___.", "(m…)", "motive"),
 G("The only ___ the burglar left behind was a bus ticket from Treviso.", "(c…)", "clue"),
 G("He booked the room under a ___ and paid in cash, so nobody at the hotel knew who he really was.", "(f… n…)", "fake name", ["fake name","false name"]),
 G("Inspector Moretti hopes to ___ before Christmas, but she still has three people on her list.", "(verbo + the c…)", "solve the case", ["solve the case","crack the case"]),
 G("The ___ of the fraud, an eighty-year-old woman, lost all her savings.", "(v…)", "victim"),
]))

# ---------------------------------------------------------------- RIPASSO A
LEVELS.append(dict(id="rA", type="review", title="⟳ RIPASSO A — criminali, reati, indagini",
 desc="i primi tre livelli insieme · frasi e definizioni nuove", items=[
 D("«a criminal who steals from people's bags and jackets on buses and trains, without them noticing» → ___", "(p…)", "pickpocket"),
 G("Somebody used my credit card details to buy plane tickets: the bank says it's a clear case of ___.", "(f…)", "fraud"),
 G("The ___ smashed the glass of the old phone box and sprayed paint on the church door.", "(v…)", "vandals"),
 D("«a person who breaks the security of computer systems, sometimes to steal data» → ___", "(h…)", "hacker"),
 G("The jewellery shop was closed for the weekend, and on Monday the owner found a big hole in the wall: thieves had ___ the shop through the bakery next door.", "(b… i…)", "broken into"),
 D("«the crime of entering someone's home illegally to take things» → ___", "(b…)", "burglary", ["burglary","burglaries"]),
 G("The police are still asking what the ___ for the attack was: the victim had no enemies and no money.", "(m…)", "motive"),
 G("Three people saw the accident at the crossing, but only one of them agreed to be a ___ in court.", "(w…)", "witness"),
 D("«a person who joins in a crime but plays a smaller part in it» → ___", "(a…)", "accomplice"),
 G("Ludovica says she didn't break the vase ___: she tripped over the cat.", "(o… p…)", "on purpose"),
 G("The camera footage didn't help: the man had a hood and dark glasses. Without a single ___, the detectives had to start again from zero.", "(c…)", "clue"),
 D("«someone who gets hurt, loses money or suffers in some other way because of what a criminal does» → ___", "(v…)", "victim"),
 G("Only three employees know the code of the safe, so the owner believes the theft was an ___.", "(i… j…)", "inside job"),
 G("On the dating app he called himself «Lorenzo», but it was a ___: his real one is Gino.", "(f… n…)", "fake name", ["fake name","false name"]),
]))

# ---------------------------------------------------------------- 04
LEVELS.append(dict(id=4, type="study", title="LIVELLO 04 — EVIDENCE AND ARRESTS",
 desc="prove, impronte, telecamere, fedina penale · indagare, arrestare, incriminare", rule=RULE, items=[
 D("«facts, objects or information that show that something is true, used in a court» → ___", "(e…)", "evidence"),
 D("«the marks that the tips of your fingers leave on glass or other surfaces» → ___", "(f…)", "fingerprints", ["fingerprints","fingerprint"]),
 D("«a camera on a wall that records what happens in a shop, bank or building» → ___", "(s… c…)", "security camera", ["security camera","security cameras","surveillance camera","surveillance cameras"]),
 D("«an official list of the crimes that a person has committed in the past» → ___", "(c… r…)", "criminal record"),
 D("«(of the police) to take someone to the police station because they think he or she has committed a crime» → ___", "(a…)", "arrest"),
 D("«(of the police) to say officially that someone has probably committed a particular crime and must go to court» → ___", "(c…)", "charge"),
 D("«to try to find out the facts about a crime» → ___", "(i…)", "investigate"),
 G("The police are sure he did it, but without ___ they can't take him to court.", "(e…)", "evidence"),
 G("Don't touch the glass! The detectives need to check it for ___ first.", "(f…)", "fingerprints"),
 G("A ___ above the cash desk filmed the shoplifter's face clearly.", "(s… c…)", "security camera", ["security camera","surveillance camera"]),
 G("You can't work at the airport if you have a ___: they check everyone's past.", "(c… r…)", "criminal record"),
 G("The officers decided to ___ the driver and took him to the station in handcuffs.", "(a…)", "arrest"),
 G("After six hours of questions, the officers ___ the young man with theft and gave him a date for his trial.", "(c…)", "charged"),
 G("Two detectives from Rome are coming to ___ the disappearance of the paintings.", "(i…)", "investigate"),
]))

# ---------------------------------------------------------------- 05
LEVELS.append(dict(id=5, type="study", title="LIVELLO 05 — IN COURT",
 desc="tribunale, processo, giudice e giuria · l'imputato, il verdetto · vincere la causa", rule=RULE, items=[
 D("«the place where a judge decides if someone is guilty of a crime» → ___", "(c…)", "court", ["court","courtroom"]),
 D("«the series of hearings in front of a judge, in which lawyers present their arguments about a crime» → ___", "(t…)", "trial"),
 D("«a court process in which everyone gets the same treatment and the judge is not on anyone's side» → ___", "(f… t…)", "fair trial"),
 D("«the person in charge of a court, who decides the punishment» → ___", "(j…)", "judge"),
 D("«a group of ordinary people, usually twelve, who decide in court if someone is guilty» → ___", "(j…)", "jury"),
 D("«the person in court who, according to the police, has committed the crime» → ___", "(t… a…)", "the accused"),
 D("«the official decision of a jury at the end of a trial» → ___", "(v…)", "verdict"),
 D("«(of a lawyer) to get the decision that he or she wanted from the court» → ___", "(w… t… c…)", "win the case"),
 G("Next Monday the two neighbours have to go to ___ because of their argument about the fence.", "(c…)", "court"),
 G("The ___ of the bank manager started in March and went on for almost a year.", "(t…)", "trial"),
 G("Everyone has the right to a ___, even a person the whole country hates.", "(f… t…)", "fair trial"),
 G("The ___ asked everyone in the room to stay silent and then read out his decision.", "(j…)", "judge"),
 G("The twelve members of the ___ discussed the evidence for two days before they reached a decision.", "(j…)", "jury"),
 G("In court, ___ sat next to his lawyer and didn't say a word.", "(t… a…)", "the accused"),
 G("After two days the jury came back into the room with its ___: «Not guilty».", "(v…)", "verdict"),
 G("Our lawyer is confident: with this new witness, she thinks she can ___.", "(verbo + the c…)", "win the case"),
]))

# ---------------------------------------------------------------- 06
LEVELS.append(dict(id=6, type="study", title="LIVELLO 06 — PUNISHMENT",
 desc="colpevole · la condanna · lavori socialmente utili, multe e celle", rule=RULE, items=[
 D("«responsible for a crime, according to a court» → ___", "(g…)", "guilty"),
 D("«the punishment that a judge gives, for example a number of years in prison» → ___", "(s…)", "sentence"),
 D("«unpaid work that a criminal must do to help the local area instead of going to prison» → ___", "(c… s…)", "community service"),
 D("«money that you must pay if you leave your car in the wrong place» → ___", "(p… f…)", "parking fine"),
 D("«a small room in a prison or a police station where they lock up a prisoner» → ___", "(c…)", "cell"),
 G("The evidence against Ms Bianchi was clear, and after only an hour the jury ___.", "(verbo + h… g…)", "found her guilty"),
 G("It was his first crime, so he got a short ___: six months, and he can spend them at home.", "(s…)", "sentence"),
 G("Instead of prison, the vandals have to do 100 hours of ___: they are cleaning the walls they painted.", "(c… s…)", "community service"),
 G("I left the car in front of the hospital entrance for ten minutes and got an 80-euro ___.", "(p… f…)", "parking fine"),
 G("The suspect spent the night in a ___ at the police station, with only a bed and a blanket.", "(c…)", "cell"),
]))

# ---------------------------------------------------------------- RIPASSO B
LEVELS.append(dict(id="rB", type="review", title="⟳ RIPASSO B — prove, tribunale, condanne",
 desc="livelli 4-6 e qualcosa di prima · frasi e definizioni nuove", items=[
 D("«information or objects which show that a person committed a crime» → ___", "(e…)", "evidence"),
 G("The officer put a fine powder on the door handle to look for ___.", "(f…)", "fingerprints"),
 G("Customers in the bank can't see it, but a ___ in the ceiling records everything.", "(s… c…)", "security camera", ["security camera","surveillance camera"]),
 D("«a list that the police keep of a person's past crimes» → ___", "(c… r…)", "criminal record"),
 G("The officers ___ the man for burglary and drove him to the police station.", "(a…)", "arrested"),
 D("«the most important official in a courtroom, who controls the trial and gives criminals their punishment» → ___", "(j…)", "judge"),
 G("Seven women and five men sit on the ___ in this case.", "(j…)", "jury"),
 G("This is a small town and everybody already thinks he's guilty: can he really get a ___ here?", "(f… t…)", "fair trial"),
 G("The jury took four days to reach a ___.", "(v…)", "verdict"),
 G("Nervous and pale, ___ stood up when the judge came in.", "(t… a…)", "the accused"),
 D("«a period of time that a judge orders a criminal to spend in prison» → ___", "(s…)", "sentence"),
 G("Our neighbour's son spent the summer painting the school fence: it was part of his ___.", "(c… s…)", "community service"),
 G("Dad stopped on the pavement outside the chemist's for two minutes and came back to a ___ on the windscreen.", "(p… f…)", "parking fine"),
 G("After a week in court, the jury ___ of fraud.", "(verbo + h… g…)", "found him guilty"),
 G("The prisoner shares a tiny ___ with two other men.", "(c…)", "cell"),
 G("This lawyer has never lost: everyone expects her to ___ again.", "(verbo + the c…)", "win the case"),
]))

# ---------------------------------------------------------------- SFIDA FINALE
LEVELS.append(dict(id="final", type="challenge", title="★ SFIDA FINALE — Crime and punishment",
 desc="tutto il lessico della unit · frasi e definizioni nuove", items=[
 G("A ___ in a balaclava threatened the cashier and ran off with the money from the safe.", "(b… r…)", "bank robber"),
 D("«a person who gets into homes illegally, often through a window, to steal valuables» → ___", "(b…)", "burglar"),
 G("Shop staff watch the cameras carefully: one ___ can take hundreds of euros of goods in a month.", "(s…)", "shoplifter"),
 G("The police think the ___ who emptied the old man's bank account works from abroad, with dozens of fake websites.", "(f…)", "fraudster"),
 G("Somebody ___ the old barn on the hill, and the flames were visible from the village.", "(verbo + f… t…)", "set fire to"),
 D("«a crime in which someone takes money from a bank or a shop by force» → ___", "(r…)", "robbery"),
 G("The man in the photo can't be the thief: he has an ___ — he was on a plane to Madrid at the time.", "(a…)", "alibi"),
 G("Inspector Galli finally ___ thanks to a single hair on the victim's coat.", "(verbo + the c…)", "solved the case", ["solved the case","cracked the case"]),
 D("«to look carefully at the facts of a crime to discover the truth» → ___", "(i…)", "investigate"),
 G("When she applied for the job at the bank, they checked if she had a ___.", "(c… r…)", "criminal record"),
 G("The police can hold a ___ at the station for 48 hours; after that, they must charge him or let him go.", "(s…)", "suspect"),
 G("After weeks of investigation, the police ___ the mayor with fraud.", "(c…)", "charged"),
 D("«the room where a trial takes place» → ___", "(c…)", "courtroom", ["courtroom","court"]),
 G("The ___ of the famous footballer begins next week, and journalists from all over Europe will be there.", "(t…)", "trial"),
 G("Both sides had good lawyers, but in the end ours ___.", "(verbo + the c…)", "won the case"),
 D("«not innocent: responsible for something bad or illegal» → ___", "(g…)", "guilty"),
 G("A tourist reported a ___ on the crowded tram: he took her phone from her backpack.", "(p…)", "pickpocket"),
 G("The judge gave the hacker a light ___: one year, and no time in prison.", "(s…)", "sentence"),
]))

# glossa: parole difficili delle definizioni e delle frasi + significato delle risposte
GLOSS = {
 "burglar":"ladro d'appartamento","bank robber":"rapinatore di banche","pickpocket":"borseggiatore",
 "shoplifter":"taccheggiatore","fraudster":"truffatore","vandals":"vandali","vandal":"vandalo",
 "hacker":"pirata informatico","accomplice":"complice","thief":"ladro","thieves":"ladri",
 "wallets":"portafogli","crowded":"affollato","tricks":"imbroglia","bus shelters":"pensiline dell'autobus",
 "benches":"panchine","without permission":"senza permesso","commit":"commettere","commits":"commette",
 "committed":"commesso","forced":"forzata","drawers":"cassetti","clown mask":"maschera da pagliaccio",
 "cashier's desk":"cassa","rush hour":"ora di punta","razors":"rasoi","spray paint":"vernice spray",
 "marks":"voti","engine running":"motore acceso",
 "burglary":"furto in appartamento","robbery":"rapina","fraud":"frode, truffa","break into":"introdursi (con la forza) in",
 "broken into":"si erano introdotti in","break-in":"effrazione, furto con scasso","set fire to":"dare fuoco a",
 "on purpose":"apposta","inside job":"colpo organizzato dall'interno","threats":"minacce","illegally":"illegalmente",
 "carried out":"messo in atto","armed":"a mano armata","smashed":"hanno sfondato","bars":"sbarre",
 "rubbish bins":"bidoni della spazzatura","fire brigade":"vigili del fuoco","by mistake":"per sbaglio",
 "employees":"dipendenti","suspects":"sospetta","pharmacy":"farmacia",
 "suspect":"sospettato","witness":"testimone","alibi":"alibi","motive":"movente","clue":"indizio",
 "fake name":"nome falso","solve the case":"risolvere il caso","solved the case":"ha risolto il caso",
 "victim":"vittima","proof":"prova","hit-and-run":"pirata della strada (incidente con fuga)",
 "number plate":"targa","petrol station":"distributore di benzina","savings":"risparmi","booked":"ha prenotato",
 "dating app":"app di incontri","footage":"riprese","hood":"cappuccio","tripped over":"è inciampata in",
 "safe":"cassaforte","theft":"furto","phone box":"cabina telefonica","sprayed":"ha spruzzato",
 "evidence":"prove","fingerprints":"impronte digitali","security camera":"telecamera di sorveglianza",
 "criminal record":"fedina penale","arrest":"arrestare","arrested":"hanno arrestato","charge":"incriminare",
 "charged":"hanno incriminato","investigate":"indagare su","tips":"punte","surfaces":"superfici",
 "handcuffs":"manette","disappearance":"scomparsa","powder":"polvere","door handle":"maniglia",
 "ceiling":"soffitto","cash desk":"cassa",
 "court":"tribunale","courtroom":"aula del tribunale","trial":"processo","fair trial":"processo equo",
 "judge":"giudice","jury":"giuria","the accused":"l'imputato","verdict":"verdetto","win the case":"vincere la causa",
 "won the case":"ha vinto la causa","lawyer":"avvocato","lawyers":"avvocati","fence":"recinzione",
 "argument":"lite","read out":"leggere ad alta voce","reach a decision":"arrivare a una decisione",
 "reached":"sono arrivati a","pale":"pallido","in charge of":"a capo di","treatment":"trattamento",
 "guilty":"colpevole","found her guilty":"l'ha giudicata colpevole","found him guilty":"l'ha giudicato colpevole",
 "sentence":"condanna, pena","community service":"lavori socialmente utili","parking fine":"multa per divieto di sosta",
 "cell":"cella","punishment":"punizione, pena","lock up":"rinchiudere","prisoner":"detenuto","blanket":"coperta",
 "unpaid":"non pagato","pavement":"marciapiede","windscreen":"parabrezza","chemist's":"farmacia",
 "balaclava":"passamontagna","threatened":"ha minacciato","goods":"merci","barn":"fienile","flames":"fiamme",
 "valuables":"oggetti di valore","by force":"con la forza","mayor":"sindaco","innocent":"innocente",
 "backpack":"zaino","tram":"tram","staff":"personale","abroad":"all'estero",
}

# Schede di studio: [voce, definizione inglese, esempio nuovo, italiano] (+ True: chunk da coprire intero)
STUDY = {
"1": [
 ["burglar", "a person who gets into a house or a flat, usually at night, to take things", "The burglar climbed in through the bathroom window.", "ladro d'appartamento"],
 ["bank robber", "a criminal who goes into a bank, often with a gun, and takes the money", "In that film the bank robber is the hero and the police are the bad guys.", "rapinatore di banche"],
 ["pickpocket", "a thief who quietly takes wallets and phones from people's bags and clothes in crowded places", "Watch your bag at the market: pickpockets love busy places.", "borseggiatore"],
 ["shoplifter", "someone who takes things from a shop without paying for them", "Big stores lose millions to shoplifters.", "taccheggiatore"],
 ["fraudster", "a person who tricks people, often online or by phone, to get their money", "Never give your bank details to strangers on the phone: they could be fraudsters.", "truffatore"],
 ["vandal", "a person who breaks or damages things in public places just for fun", "Vandals broke the swings in the playground again.", "vandalo"],
 ["hacker", "someone who gets into other people's computers or online accounts without permission", "A hacker stole the passwords of thousands of users.", "hacker, pirata informatico"],
 ["accomplice", "a person who helps someone else to commit a crime", "The police are still looking for his accomplice.", "complice"],
],
"2": [
 ["burglary", "the crime of getting into a building to take things", "Burglary is more common in the holiday months.", "furto in appartamento"],
 ["robbery", "the crime of taking money or things from a person or a place, often with violence or threats", "The robbery took only three minutes.", "rapina"],
 ["fraud", "the crime of tricking people to get money from them", "Online fraud is growing fast.", "frode, truffa"],
 ["break into", "to enter a building or a car illegally, often by damaging a door or a window", "Thieves often break into cars near the beach.", "introdursi (con la forza) in, scassinare", True],
 ["break-in", "an occasion when someone enters a building illegally to take something", "There was a break-in at the gym over the weekend.", "effrazione, furto con scasso"],
 ["set fire to", "to make something start burning, usually on purpose", "Who would set fire to a forest?", "dare fuoco a", True],
 ["on purpose", "not by accident; because you really wanted to do it", "Sorry, I didn't step on your foot on purpose!", "apposta"],
 ["inside job", "a crime that someone plans or commits from inside the place where they work", "The detective soon understood that it was an inside job.", "colpo organizzato dall'interno"],
],
"3": [
 ["suspect", "a person who the police think may be guilty of a crime", "The main suspect has disappeared.", "sospettato"],
 ["witness", "someone who sees a crime or an accident and can describe what happened", "The witness gave a clear description of the car.", "testimone"],
 ["alibi", "proof that you were in a different place when a crime happened", "She has a perfect alibi: she was on stage in front of 500 people.", "alibi"],
 ["motive", "the reason why someone commits a crime", "Money is the most common motive.", "movente"],
 ["clue", "a small piece of information or an object that helps to find the answer to a mystery", "In this game you follow the clues to find the treasure.", "indizio"],
 ["fake name", "a name that is not your real one, which you use to hide who you are", "Lots of people use a fake name on social media.", "nome falso"],
 ["solve the case", "to find out who committed a crime and how", "Will the young detective solve the case before the end of the book?", "risolvere il caso", True],
 ["victim", "a person who suffers because of a crime", "The victim of the theft was a tourist from Japan.", "vittima"],
],
"4": [
 ["evidence", "facts, objects or information that show that something is true, used in a court", "There isn't enough evidence to take her to court.", "prove"],
 ["fingerprints", "the marks that the tips of your fingers leave on glass or other surfaces", "Each person has unique fingerprints, even twins.", "impronte digitali"],
 ["security camera", "a camera on a wall that records what happens in a shop, bank or building", "There are security cameras at both entrances of the station.", "telecamera di sorveglianza"],
 ["criminal record", "an official list of the crimes that a person has committed in the past", "My cousin has a clean criminal record and wants to join the police.", "fedina penale"],
 ["arrest", "to take someone to the police station because they think he or she has committed a crime", "The police arrested two men near the border.", "arrestare"],
 ["charge someone with", "charge: to say officially that someone has probably committed a particular crime and must go to court", "They charged the driver with dangerous driving.", "incriminare qualcuno per"],
 ["investigate", "to try to find out the facts about a crime", "Firefighters and police will investigate the cause of the fire at the factory together.", "indagare su"],
],
"5": [
 ["court", "the place where a judge decides if someone is guilty of a crime", "You can't take photos in court.", "tribunale"],
 ["trial", "the series of hearings in front of a judge, in which lawyers present their arguments about a crime", "The trial starts on 4 May.", "processo"],
 ["fair trial", "a court process in which everyone gets the same treatment and the judge is not on anyone's side", "Without good lawyers, there is no fair trial.", "processo equo"],
 ["judge", "the person in charge of a court, who decides the punishment", "The judge listened to both sides.", "giudice"],
 ["jury", "a group of ordinary people, usually twelve, who decide in court if someone is guilty", "My aunt was on a jury in London once.", "giuria"],
 ["the accused", "the person in court who, according to the police, has committed the crime", "The accused smiled at the photographers outside.", "l'imputato"],
 ["verdict", "the official decision of a jury at the end of a trial", "The families waited outside for the verdict.", "verdetto"],
 ["win the case", "to get the decision that you wanted from the court", "Lawyers don't always win the case, even with strong evidence.", "vincere la causa", True],
],
"6": [
 ["find someone guilty", "guilty: responsible for a crime, according to a court", "The court found the company guilty of polluting the river.", "giudicare colpevole qualcuno"],
 ["sentence", "the punishment that a judge gives, for example a number of years in prison", "He is now serving a ten-year sentence.", "condanna, pena"],
 ["community service", "unpaid work that a criminal must do to help the local area instead of going to prison", "Community service can teach young offenders to respect their town.", "lavori socialmente utili"],
 ["parking fine", "money that you must pay if you leave your car in the wrong place", "My dad pays at least one parking fine a month.", "multa per divieto di sosta"],
 ["cell", "a small room in a prison or a police station where they lock up a prisoner", "The cell had a tiny window high up in the wall.", "cella"],
],
}
