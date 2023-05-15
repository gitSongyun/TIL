

def pick(n, picked, topick):
    if topick == 0:
        v = list()
        for p in picked:
            v.append(number[p])
        lst.append(v)

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            pick(n, picked + [i], topick - 1)



# 조합
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

# 순열
# def pick(n, picked, topick):
#     if topick == 0:
#         v = list()
#         for p in picked:
#             v.append(number[p])
#         lst.append(v)
#         return
#
#
#     for i in range(n):
#         if i not in picked:
#             pick(n, picked + [i], topick - 1)

lst = []
number = [1, 2, 9, 5]
pick(4, [], 2)
print(lst)

l = ['a', 'a', 'c', 'd']
n = len(l)
r = 2
answer = []

def dfs(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return

    for i in range(idx, n):
        dfs(i+1,list+[l[i]])

dfs(0, [])
print(answer)

# def pick(n, picked, topick):
#     if topick == 0:
#         ans = picked[:]
#         return ans
#
#     if not picked:
#         smallest = 0
#     else:
#         smallest = picked[-1]
#
#     for i in range(smallest, n):
#         if i not in picked:
#             picked.append(i)
#             pick(n, picked, topick -1)
#             picked.pop()