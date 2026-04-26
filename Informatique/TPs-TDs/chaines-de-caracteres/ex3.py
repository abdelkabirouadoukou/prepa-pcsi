phrase ="une comme chat chat de pur chat chat"
def compter(phrase):
    l=phrase.split() # note: dont use `phrase.split(" ")` for example "chat  chat" will show ['chat', '', '', 'chat']
    print(l)
    return len(l)
print(compter(phrase))