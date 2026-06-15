def creerPile():
    return []
def estVide(pile):
    return pile == []
def sommet(pile):
    return pile[-1]
def empiler(pile, elt):
    return pile.append(elt)
def depiler(pile):
    pile.pop()