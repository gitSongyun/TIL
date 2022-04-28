def push(stack, item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("unerflow")
        return 0
    else:
        top -= 1
        return arr_1[top+1]


# size 10짜리 스택을 만들 거다
size = 10
# 내용물이 0인 스택 생성
arr_1 = [0] * size
# push를 하면 +1을 할 것이기 때문에 -1층 부터 시작
top = -1

push(arr_1, 10, size)
push(arr_1, 20, size)
push(arr_1, 30, size)

print(pop())
print(pop())
print(pop())



