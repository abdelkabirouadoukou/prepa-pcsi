def enlever_espace(phrase):
    l=phrase.split()
    new_phrase=""
    for i in range(len(l)-1):
        new_phrase += l[i]+" "+l[i+1]
    return new_phrase
print(enlever_espace("bon jo   how s   sh"))