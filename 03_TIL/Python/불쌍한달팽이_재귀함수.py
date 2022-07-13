def snail(height, day, night, cnt =1):
        # 재귀 종료 지점 생성
        if height <= day:
            return cnt
        # 재귀 생성
        else: 
            
            height -= (day-night)
            return snail(height,day,night, cnt+1)
        
print(snail(100, 5, 2))

# # 총장님 코드 (기밀)
# def snail(height, day, night, cnt=1):
#     height -= day

#     if height <= 0:
#         return cnt

#     height += night

#     return snail(height, day, night, cnt+1)
# print(snail(100, 5, 2))