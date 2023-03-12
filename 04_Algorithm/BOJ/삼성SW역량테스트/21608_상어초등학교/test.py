# 테스트 케이스 생성기
import random
ch=[]
print(10)
for i in range(100):
    a=[]
    s=0
    while len(a)<5:
        x=random.randint(1,9)
        if s==0 :
            if x not in ch:
                a.append(x)
                s+=1
        elif x not in a:
            a.append(x)
        
    ch.append(a[0])
    for i in range(5):
        if i<4:
            print(a[i],end=' ')
        elif i==4:
            print(a[i],end='\n')