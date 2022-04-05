# 큐-구현 풀이
# 2022-02-25


# 가장 앞에 있는 원소를 검색하여 반환하는 함수(검색)
def Qpeek():
    if front == rear:
        print('Queue_Empty')
    else:
        return Q[front+1]


# 비었는지 확인하는 함수(공백상태)
def isEmpty():
    return front == rear


# 가득인지 확인하는 함수(포화상태)
def Full():
    return rear == len(Q) - 1


# 삽입
def enQueue(item):
    global rear

    if rear == len(Q)-1:
        return 'Queue_Full'
    else:
        rear += 1
        Q[rear] = item


# 삭제
def deQueue():

    global front
    global rear

    if front == rear:
        return 'Queue_Empty'
    else:
        front += 1
        return Q[front]


N = 3               # 주어진 조건
Q = [0]*N
front = rear = -1

enQueue('가')
enQueue('나')

print(deQueue())
print(deQueue())
print(enQueue('나'), Q)
