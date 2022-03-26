n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#    좌 하 우 상

d = -1
out = 0
# grid = [[0]*n for _ in range(n)]
# grid_idx = 0
while 0 <= x < n and 0 <= y < n:
    d += 1
    l = d // 2 + 1
    for _ in range(l):
        nx = x + dx[d % 4]
        ny = y + dy[d % 4]
        if ny == -1:
            y = ny
            break
        # grid_idx +=1
        # grid[nx][ny] = grid_idx

        if lst[nx][ny] > 0:
            cnt = 0
            # 1 %
            for tmp_d in [1, -1]:
                nd = (d + tmp_d) % 4
                nnx = x + dx[nd]
                nny = y + dy[nd]
                if 0 <= nnx < n and 0 <= nny < n:
                    lst[nnx][nny] += int(lst[nx][ny] * 0.01)
                else:
                    out += int(lst[nx][ny] * 0.01)
                cnt += int(lst[nx][ny] * 0.01)
            # 7%
            for tmp_d in [1, -1]:
                nd = (d + tmp_d) % 4
                nnx = nx + dx[nd]
                nny = ny + dy[nd]
                if 0 <= nnx < n and 0 <= nny < n:
                    lst[nnx][nny] += int(lst[nx][ny] * 0.07)
                else:
                    out += int(lst[nx][ny] * 0.07)
                cnt += int(lst[nx][ny] * 0.07)
            # 2%
            for tmp_d in [1, -1]:
                nd = (d + tmp_d) % 4
                nnx = nx + dx[nd] * 2
                nny = ny + dy[nd] * 2
                if 0 <= nnx < n and 0 <= nny < n:
                    lst[nnx][nny] += int(lst[nx][ny] * 0.02)
                else:
                    out += int(lst[nx][ny] * 0.02)
                cnt += int(lst[nx][ny] * 0.02)
            # 10%
            nnx = nx + dx[d % 4]
            nny = ny + dy[d % 4]
            for tmp_d in [1, -1]:
                nd = (d + tmp_d) % 4
                nnnx = nnx + dx[nd]
                nnny = nny + dy[nd]
                if 0 <= nnnx < n and 0 <= nnny < n:
                    lst[nnnx][nnny] += int(lst[nx][ny] * 0.10)
                else:
                    out += int(lst[nx][ny] * 0.10)
                cnt += int(lst[nx][ny] * 0.10)
            # 5%
            nnx = nx + dx[d % 4] * 2
            nny = ny + dy[d % 4] * 2
            if 0 <= nnx < n and 0 <= nny < n:
                lst[nnx][nny] += int(lst[nx][ny] * 0.05)
            else:
                out += int(lst[nx][ny] * 0.05)
            cnt += int(lst[nx][ny] * 0.05)
            # alpha
            nnx = nx + dx[d % 4]
            nny = ny + dy[d % 4]
            if 0 <= nnx < n and 0 <= nny < n:
                lst[nnx][nny] += lst[nx][ny] - cnt
            else:
                out += lst[nx][ny] - cnt
            lst[nx][ny] = 0
        x, y = nx, ny

print(out)


# 순열 조합
def pick(n, picked, toPick):
    if toPick == 0:
        return print(picked)

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.pop()


# 순서가 없는 비복원 추출
def pick2(n, picked, toPick):
    if toPick == 0:
        return print(picked)

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick2(n, picked, toPick - 1)
            picked.pop()


# 순서가 있는 복원 추출
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
pick(3, [], 2)
print('순서가 없는 비복원 추출')
pick2(3, [], 2)
print('순서가 있는 복원 추출')
pick3(3, [], 2)
print('순서가 있는 비복원 추출')
pick4(3, [], 2)