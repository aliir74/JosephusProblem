#solve Josephus permutation with specified start
def showSequence(l, first):
    #l2 = copy.deepcopy(l)
    l2 = []
    for i in range(len(l)):
        if(l[i] != -1):
            l2.append(l[i])
    print(l2)
    if(len(l2) == 1):
        return l2[0]
    for i in range(first, len(l2), 2):
        l2[i] = -1
        tmp = i

    if(tmp == len(l2)-2):
        f = 0
        #l2[0] = -1
    else:
        f = 1

    x = []
    for i in range(len(l2)):
        if(l2[i] != -1):
            x.append(l2[i])
    #print(l2)
    return showSequence(x, f)

l = []
for i in range(1, 101):
    l.append(i)
    x = showSequence(l, 0)
    print(i, ' : ', x)
    print('\n\n\n')

