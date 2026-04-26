def doubler(chaine):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    newchaine=""
    for i in range(len(chaine)):
        if chaine[i] in voyelles:
            newchaine += chaine[i]*2
        else:
            newchaine += chaine[i]
    return newchaine
print(doubler("glouglou dit le dindon"))