from collections import Counter
def solution(nums):
    answer = 0
    # 절반의 포켓몬 선택 가능
    # 종류는 최대한 많게
    if len(nums) // 2 >=len(Counter(nums)):
        answer = len(Counter(nums))
    else :
        answer = len(nums) // 2
    return answer

# nums = [3,3,3,2,2,4]