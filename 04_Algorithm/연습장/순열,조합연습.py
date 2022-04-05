def pick(n, picked, topick):

    if topick == 0:
        return picked

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]

    for i in range(smallest, n):

        if i not in picked:
            picked.append(i)
            pick(n, picked, topick-1)
            picked.pop()



def pick(n, picked, topick):
    if topick == 0:
        v = list()
        for p in picked:
            v.append(number[p])
        lst.append(v)
        return

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            pick(n, picked + [i], topick - 1)


lst = []
number = [1, 3, 9]
pick(3, [], 2)
print(lst)


def pick(n, picked, topick):
    if topick == 0:
        ans = picked[:]
        return ans

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick(n, picked, topick -1)
            picked.pop()