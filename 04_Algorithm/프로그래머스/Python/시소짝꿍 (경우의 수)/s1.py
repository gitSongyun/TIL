from collections import Counter
def solution(weights):
    answer = 0
    # 각 숫자에 1, 2, 3, 4를 곱햇을 때 값이 같아지면 된다. 
    # 공배수인지 판별, 둘의 공배수가 곱하기 2, 3, 4 안에 있냐?
    dict = Counter(weights)
    
    ws = list(dict.keys())
    for i in range(len(dict)):
        for j in range(i, len(dict)):
            
            a , b = ws[i], ws[j]
            # 두 수가 같은 경우 
            if i == j and dict[a] > 1:
                answer += dict[a] * (dict[a] - 1) // 2
                continue
            
            if a*2 == b*3:
                answer += dict[a] * dict[b]
            if a*2 == b*4:
                answer += dict[a] * dict[b]
            if a*3 == b*2:
                answer += dict[a] * dict[b]
            if a*3 == b*4:
                answer += dict[a] * dict[b]
            if a*4 == b*2:
                answer += dict[a] * dict[b]
            if a*4 == b*3:
                answer += dict[a] * dict[b]
    print(answer)
            
                
    
    return answer

#     weights	result
# [100,180,360,100,270]	4