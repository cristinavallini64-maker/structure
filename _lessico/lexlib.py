# Funzioni comuni ai file di lessico della Structure (lessico-uN.html).
I_DEF = "Scrivi la parola che corrisponde alla definizione."
I_WORD = "Completa la frase con la parola che manca."
I_CHUNK = "Completa la frase con il verbo e la parola giusti."
PDG = {"play","plays","played","do","does","did","go","goes","went"}
CFG = {"split_pdg": False}   # solo Unit 1: play/do/go stanno negli Esercitati

def D(q, hint, a, acc=None):
    """Definizione inglese -> parola o chunk. hint = iniziali, es. (m… b…)"""
    return ("def", q, hint, a, acc or [a])

def G(q, hint, a, acc=None, ins=I_WORD):
    """Frase con buco. Se hint comincia con '(verbo + ', la risposta e' un chunk
    verbo + parola da produrre intero (il verbo non ha iniziale)."""
    acc = acc or [a]
    if hint.startswith("(verbo + ") and not (CFG["split_pdg"] and a.split()[0] in PDG):
        ins = I_CHUNK
    elif hint.startswith("(verbo + "):
        k = hint.count("…")
        w = a.split(); pre = " ".join(w[:-k]); noun = " ".join(w[-k:])
        q = q.replace("___", pre + " ___", 1)
        acc = list(dict.fromkeys(x[len(pre)+1:] for x in acc if x.startswith(pre + " ")))
        hint = "(" + " ".join(t for t in hint[len("(verbo + "):-1].split() if "…" in t) + ")"
        a = noun
    return ("gap", q, hint, a, acc, ins)

RULE_STD = ("<strong>COME SI LAVORA</strong><br>"
        "&#x2714; <strong>Definizione</strong>: leggi la descrizione in inglese e scrivi la parola. "
        "Fra parentesi trovi le iniziali: una lettera per ogni parola della risposta.<br>"
        "&#x2714; <strong>Frase</strong>: completa con la parola che manca. Anche qui fra parentesi ci sono le iniziali. "
        "Se c'&egrave; scritto <em>verbo +</em>, devi scrivere anche il verbo giusto.<br>"
        "&#x2714; Prima degli esercizi puoi aprire <strong>&#x1F4D6; Studia le parole</strong> dalla mappa.<br>"
        "&#x26A0; Se sbagli, l'esercizio torna alla fine del giro: dopo la correzione prova a ricordare la parola.")
