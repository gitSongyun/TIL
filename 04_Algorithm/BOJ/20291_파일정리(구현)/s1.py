import sys
sys.stdin = open('input.txt')

""" 내풀이
from collections import Counter
N = int(input())
tmp_arr = []
for i in range(N):
    file = input()
    dot_idx = file.index('.')
    type = file[dot_idx+1:]
    tmp_arr.append(type)


ans = Counter(tmp_arr)
answer = []
for key, val in ans.items():
    answer.append([key, val])

answer.sort()

for a in answer:
    print(a[0], a[1])
"""

""" 참고 풀이
input = sys.stdin.readline
DICT = dict()
n = int(input())
for i in range(n):
    name, ext = input().strip().split('.')
    print(name, ext)
    DICT[ext] = DICT.get(ext, 0) + 1

print('\n'.join(a + ' ' + str(DICT[a]) for a in sorted(DICT.keys())))
"""
