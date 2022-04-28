# 문자열뒤집기 풀이
# 2022-02-16

s = 'Reverse this strings'
s = s[::-1]
print(s)

# reverse를 사용하려면 각 문자를 리스트에 담아서 사용한다.
a = list(s)
a.reverse()
for i in a:
    print(i, end='')
print()