import sys

N, M = map(int, sys.stdin.readline().split())
roomName = []
# 회의실 종류 
for _ in range(N):
    roomName.append(str(sys.stdin.readline().rstrip().lstrip()))

# 예약정보 기본값 설정
roomCode1 = dict()
for i in roomName:
    roomCode1[i] = [[9], [18]]

# 회의실 이름 사전 순 정렬
roomCode1 = dict(sorted(roomCode1.items(), key=lambda x : x[0]))

# 예약정보 입력
for _ in range(M):
    room, start, end = map(str, sys.stdin.readline().split())
    start = int(start)
    end = int(end)
    
    # 예약 시작시간은, 가능한 시간대의 끝시간이되고
    roomCode1[room][0].append(end)
    # 예약 끝 시간은, 가능한 시간대의 시작시간이 된다. 
    roomCode1[room][1].append(start)

# 마지막 값에 하이픈 안넣기 위한 cnt
cnt = 0
for key, value in roomCode1.items():
    cnt += 1
    # 예약가능한 시간대를 넣기 위한 리스트
    time = []
    # 예약가능시간(시작시간, 끝시간) 정렬
    roomCode1[key][0].sort()
    roomCode1[key][1].sort()

    for s, e in list(zip(roomCode1[key][0], roomCode1[key][1])):
        # 예악가능시간의 시작시간이 끝시간 보다 작을때, 예약 가능함
        if s < e:
            time.append([str(s).zfill(2), str(e).zfill(2)])

    print(f'Room {key}:')

    # 예약 가능한 시간대가 없는 경우
    if len(time) == 0:
        print('Not available')
        print('-----')
        
    else:  
        print(f'{len(time)} available:')
        for t in time:
            print(f'{t[0]}-{t[1]}')
    
        
        # 마지막 회의실 정보에서 하이픈은 안넣는다.
        if cnt < len(roomName):
            print('-----')
        else: 
            break

 
# 입력 1  
# 3 7
# grandeur
# avante
# sonata
# sonata 14 16
# grandeur 11 12
# avante 15 18
# sonata 10 11
# avante 9 12
# grandeur 16 18
# avante 12 15

# 출력 2
# 3 2
# santafe
# aerocity
# porter
# santafe 9 12
# porter 9 18