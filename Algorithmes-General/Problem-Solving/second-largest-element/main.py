# if `.sort()` fonction is allowed
def SecondLargestElement_sort(l):
    l.sort()
    r = 0
    for i in range(0, len(l)):
        if l[-1] == l[i]:
            r += 1
        else: continue
    print(l[-r - 1])


print(SecondLargestElement_sort([10, 5, 20, 20, 20, 20, 20, 8]))


# if not
def SecondLargestElement_nonsort(l):
    if len(l) < 2:
        return None

    # in this part Dont ask me how this's work :)
    l2 = l[:]
    for i in range(len(l2)):
        for j in range(0, len(l2) - i - 1):
            if l2[j] > l2[j + 1]:
                l2[j], l2[j + 1] = l2[j + 1], l2[j]
    
    r = 0
    for i in range(0, len(l2)):
        if l2[-1] == l2[i]:
            r += 1
        else:
            continue
    return l2[-r - 1]


print(SecondLargestElement_nonsort([10, 5, 20, 20, 20, 20, 20, 8]))

# [1/11/2026] I will update this code, I make this complexe so i am thinking how can i make it easyer :)
