# 문제가 너무 귀여워 로봇들이 불쌍해
# 난 이렇게 귀여운 문제만 봐도 행복해하는 사람인데 이 세상이 나를
def minimum_time_to_finish(commands):
    # 로봇의 초기 위치와 시간을 초기화
    o_pos, b_pos = 1, 1  # 오렌지와 블루의 초기 위치
    o_time, b_time = 0, 0  # 오렌지와 블루의 초기 시간
    total_time = 0

    for command in commands:
        robot, target_pos = command[0], int(command[1]) # 얘는 int해줘야 함
        
        if robot == 'O':
            # 오렌지가 이동해야 하는 거리와 시간
            move_time = abs(target_pos - o_pos)
            o_time = max(total_time, o_time + move_time) + 1
            total_time = o_time
            o_pos = target_pos
        else:  # robot == 'B'
            # 블루가 이동해야 하는 거리와 시간
            move_time = abs(target_pos - b_pos)
            b_time = max(total_time, b_time + move_time) + 1
            total_time = b_time
            b_pos = target_pos
    
    return total_time

# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    data = input().split()
    N = int(data[0])
    # int로 받으면 안됨
    commands = [(data[i], data[i + 1]) for i in range(1, 2 * N, 2)]
    
    result = minimum_time_to_finish(commands)
    print(f'#{tc} {result}')