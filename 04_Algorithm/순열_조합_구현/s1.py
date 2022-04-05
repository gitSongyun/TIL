# 순서가 없는(조합) 복원 추출
def pick(n, picked, toPick):

    # 만약 toPick 이 0이 되면
    if toPick == 0:
        ans = picked[:]
        return print(ans)

    # picked 가 빈 상태면
    if not picked:
        smallest = 0

    # picked 안에 원소가 존재한다면
    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.pop()


# 순서가 없는 비복원 추출
def pick2(n, picked, toPick):
    if toPick == 0:
        return print(picked)

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick2(n, picked, toPick - 1)
            picked.pop()


# 순서가 있는(순열) 복원 추출
def pick3(n, picked, toPick):

    if toPick == 0:
        return print(picked)

    for i in range(n):
        picked.append(i)
        pick3(n, picked, toPick - 1)
        picked.pop()




# 순서가 있는 비복원 추출
def pick4(n, picked, toPick):

    if toPick == 0:
        return print(picked)

    for i in range(n):
        if i not in picked:
            picked.append(i)
            pick4(n, picked, toPick - 1)
            picked.pop()


print('순서가 없는 복원 추출')
# 0~2 , 2개를 뽑겠다.
pick(3, [], 2)
print('순서가 없는 비복원 추출')
pick2(3, [], 2)
print('순서가 있는 복원 추출')
pick3(3, [], 2)
print('순서가 있는 비복원 추출')
pick4(3, [], 2)