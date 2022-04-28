p = 'mike'
t = 'My mike is very good'
M = len(p)
N = len(t)

def serch_pattern(p, t):
    i = 0
    j = 0
    # j는 패턴의 idx, i는 전체 문자열의 idx
    while j < M and i < N:
        # 만약 문자열과 패턴의 글자가 같지 않다면
        if t[i] != p[j]:
            # 현재검사중인 위치에서 이미 검사한 패턴의 수만큼 빼준다.
            # 패턴과 전체 문자가 서로 같기 시작한 시점 이후 부터 시작하기 위해
            i = i - j
            # j는 0번 인덱스부터 시작하기 위해 -1을 한다.
            j = -1
        # 비교값이 같다면 다음인덱스를 비교하기 위해 1을 더한다.
        i += 1
        j += 1

    if j == M:
        return i-M

    else:
        return -1

print(serch_pattern(p, t))