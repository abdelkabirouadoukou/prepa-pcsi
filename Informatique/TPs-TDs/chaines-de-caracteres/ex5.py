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

# adv one
def doubler_adv(chaine):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    return ''.join(char*2 if char in voyelles else char for char in chaine)