L=[2,123,-12,2,-0,1]
def Lemin(l,i):
    key=i
    for j in range(i,len(l)):
        if l[j] < l[key]:
            key = j
    return key
print(Lemin(L,3))

def selection(l):
    for i in range(len(l)):
        mini_index=Lemin(l, i)
        if l[i] > l[mini_index]:
            l[i],l[mini_index]=l[mini_index],l[i]
    return l
print(selection(L))

def TriSelection(l):
    for i in range(len(l)):
        mini_index=i
        for j in range(i,len(l)):
            if l[j] < l[mini_index]:
                mini_index = j
        if l[i] > l[mini_index]:
            l[i],l[mini_index]=l[mini_index],l[i]
    return l
print(TriSelection(L))