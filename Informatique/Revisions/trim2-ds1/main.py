# with count
def estEnsembles_count(l):
    for i in range(0, len(l)):
        if l.count(l[i])>=2:
            return False
    return True

print(estEnsembles_count([1,2,3]))

def estEnsembles_without_count(l):
    new_list=[]
    for i in range(0, len(l)):
        if l[i] not in new_list:
            new_list.append(l[i])
        else: return False
    return True

print(estEnsembles_without_count([1,2,3,1]))

def estEnsembles_rec(l):
    if len(l)==0:
        return True
    for i in range(1,len(l)):
        if l[0] == l[i]:
            return False   
    return estEnsembles_rec(l[1:])

print(estEnsembles_rec([1,2,3,1 ]))