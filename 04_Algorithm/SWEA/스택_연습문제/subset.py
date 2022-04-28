def f(i, N):
    if i == N:

        for j in range(N):
            if bit[j]:
                print(a[j], end= '')
        print()

    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

    return

a = [1, 2, 3]
bit = [0, 0, 0]
f(0, 3)