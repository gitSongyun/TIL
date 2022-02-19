# Babyjin.py 풀이
# 2022-02-09

# 연속된 숫자의 카드이면 run, 같은 숫자의 카드가 3장이면 triplet

# 6장의 카드를 list로 생성
num = list(map(int, input()))
# 10칸이 필요하지만 run 판별시 j+2를 사용하므로 2개를 더 만들어 index error를 피한다.
counts = [0] * 12

run=tri=0

for i in range(6):
    #  카드에 같은 수가 몇 개 있는지 파악해야 함. counts의 인덱스와 내용은 카드의 숫자와 갯수에 대응.
    counts[num[i]]+= 1

for j in range(1, 10):

    # triplet 판별
    if counts[j] >=3: # 같은 숫자의 카드가 3장 이상이라면 tri 이므로
        tri+=1
        counts[j]-=3 # triplet으로 카드를 썼으므로 3장을 없앤다.
        continue

    # run 판별
    if counts[j]>0 and counts[j] == counts[j+1] == counts[j+2]: # 카드 갯수가 1장 이상이고, 연속된 숫자라면
        run+=1
        # run으로 연속된 숫자의 카드 1장씩 썼으므로 빼준다.
        counts[j]-=1
        counts[j+1]-=1
        counts[j+2]-=1
        continue

# 결과 출력
print("tri : ", tri , "run : ", run)

if tri+run >= 2:
    print("Baby-jin")

else:
    print("Lose")

