def longeur_rec(chaine):
    if chaine=="":
        return 0
    else:
        return longeur_rec(chaine[:-1])+1
print(longeur_rec("sasssd"))

def longeur_ite(chaine):
    count=0
    for x in chaine:
        count+=1
    return count
print(longeur_ite("ddds"))

