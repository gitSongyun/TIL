from collections import deque
N = 4 # 카드를 몇 번 버릴 건지

card = deque()
for i in range(1, N+1):
    card.append(i)
print(card)
card.popleft()
print(card[0])
print(card)

# while len(card) > 1:
#     print(card)
#     card.popleft()
#     temp = card[]
#     # card = card[1:len(card)]
#     card.append(temp)


# print(card[0])


