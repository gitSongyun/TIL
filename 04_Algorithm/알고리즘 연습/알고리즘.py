# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         print(bin(i), bin(1<<j),j)
#         if i&(1<<j):
#             print(arr[j], end='   ')
#
#     print()


# ***전치행렬 만들기***
# arr = [[4,1,3], [1,4,2]]
#
# arr = list(zip(*arr))
# print(arr)

def fibo1(n):
    global memo

    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n - 1) + fibo1(n - 2))
    return memo[n]


memo = [0, 1]
a = fibo1(6)
print(a)