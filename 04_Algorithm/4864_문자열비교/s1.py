# 4864_문자열비교 풀이
# 2022-02-17
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

#
def length(para_str):
    ans = 0
    for k in para_str:
        ans += 1
    return ans


for t in range(1, T+1):

    str1 = list(map(str,input()))
    str2 = list(map(str,input()))

    len_1 = length(str1)
    len_2 = length(str2)


    # 같으면 두번째 반복문 끝내고 첫번째 반복문으로 넘어감

    cnt = 0
    i = j = 0

    for i in range(i, len_1):

        for j in range(j, len_2):

            if str1[i] == str2[j]:
                cnt += 1
                i += 1
                j += 1
                break

            if str1[i] != str2[j] and cnt != 0:
                j = j - 1
                i = 0
                cnt = 0

            else:
                j = j
                i = 0
                cnt = 0

    if cnt == len_1:
        print("#{} 1" .format(t))
    else:
        print("#{} 0" .format(t))





    # cnt=0
    # for i in str1:
    #
    #     if cnt == len_1:
    #         break
    #
    #     for j in str2:
    #         if i == j:
    #             cnt += 1
    #             break
    #
    #         else:
    #             cnt = 0
    # print(cnt)
