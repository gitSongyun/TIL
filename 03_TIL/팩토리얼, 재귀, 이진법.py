## while 문을 이용한 factorial
# def fact(a):
#     i = 1
#     if a == 1:
#         return 1
    
#     while a>1:
#         i*=a
#         a-=1
#     return i
# print(fact(5))


## 재귀함수를 이용한 facorial
# def factorial(a,i=1):
#     if a == 1:
#         return 1
#     else:
#         return a*factorial(a-1)
# fib(10)


## for문을 이용힌 피보나치 수열의 합
# def fib_loop(a):
#     if a < 2:
#         return a
#     base_list=[0,1]
#     for i in range(2,a+1): #2~10 
#         base_list.append( base_list[i-1]+ base_list[i-2])  
#     return base_list[-1]
# print(fib_loop(3))


## 재귀함수를 이용한 피보나치 수열
# 1 1 2 3 5 8 13
# def fib(a):
#     if a < 2:
#         return a
#     else:
#         return fib(a-1)+fib(a-2)

# print(fib(10))


## 재귀로 십진법을 이진법으로 구하기 (list 이용)
# 0b1110
# def bin1(a, list_1=[]):
#     if a==1:
#         list_1.append(1)
#         return list_1[::-1]
         
#     else:
#         list_1.append(a%2)
#         a=a//2
#         return bin1(a, list_1) 
#print(bin1(18))


## 재귀로 십진법을 이진법으로 만들기 (str 이용)
# def bin1(a, str_1=''):
    
#     str_1 += str(a%2) # 나머지를 str_1에 넣는다.
#     if a==1:
#         return str_1[::-1] # 나머지를 구한 순서대로 str_1에 넣은 후 반대로 출력하면 이진법 완성
    
#     a=a//2 # 몫을 구한 후 그 값을 다시 함수로 호출한다.
#     return bin1(a, str_1) 

# print(bin1(18)) #10010


## 반복문으로 이진법을 십진법으로 만들기
# def decimal(a):
#     str1=str(a)
#     str2=str1[::-1] # 1 1 0 1
#     cnt=0
#     j=0
#     for i in str2: # i = '1','1','0','1' 
#         if i == '1': # i = '1' 이라면 
#             cnt+=2**j # cnt에 2^j 를 더해 주겠다.
#             j+=1      # 그리고 j를 1올린다.
#         else:
#             j+=1      # 1이 아니라면 j만 1 더해준다.
#     return cnt
# print(decimal(11110))