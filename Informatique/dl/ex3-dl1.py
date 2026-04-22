def k_mer(text, k):
    dico = {}
    for i in range(len(text) - k + 1):
        sous_chaine= text[i:i+k]
        dico[i+1] =sous_chaine
    return dico

def estExiste(text, ch):
    k = len(ch)
    repertoire =k_mer(text, k)
    return ch in repertoire.values()

def decalage(text, ch):
    indices=[]
    k =len(ch)
    repertoire = k_mer(text, k)
    for cle,valeur in repertoire.items():
        if valeur== ch:
            indices.append(cle - 1)
    return indices

t = "ACTGTTAGCAAXTAGGWTSHSTGH"
print(decalage(t, "TAG"))
