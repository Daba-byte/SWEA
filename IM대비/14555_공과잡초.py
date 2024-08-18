T = int(input())
for tc in range(1, T + 1):
    grassland = input()

    ball_count = 0
    i = 0
    while i < len(grassland) - 1:
        if grassland[i] == '(':
            if i + 1 < len(grassland) and grassland[i + 1] == ')':
                # '()' 형태의 공 발견
                ball_count += 1
                i += 2  # 이미 찾은 공을 건너뛰기 위해 2칸 전진
            elif i + 1 < len(grassland) and grassland[i + 1] == '|':
                # '(|' 형태 발견 -> 최소한 하나의 공이 있을 수 있음
                ball_count += 1
                i += 1  # 현재 위치에서 한 칸만 이동
            else:
                i += 1
        elif grassland[i] == '|' and i + 1 < len(grassland) and grassland[i + 1] == ')':
            # '|)' 형태 발견 -> 최소한 하나의 공이 있을 수 있음
            ball_count += 1
            i += 2  # 이미 찾은 공을 건너뛰기 위해 2칸 전진
        else:
            i += 1

    print(f'#{tc} {ball_count}')

##### for문으로 #####

T = int(input())
for tc in range(1, T + 1):
    grassland = input()

    ball_count = 0
    i = 0
    n = len(grassland)

    for i in range(n):
        if grassland[i] == '(':
            if i + 1 < n and grassland[i + 1] == ')':
                # '()' 형태의 공 발견
                ball_count += 1
                i += 1  # 이미 찾은 공을 건너뛰기 위해 인덱스 한 칸 더 이동
            elif i + 1 < n and grassland[i + 1] == '|':
                # '(|' 형태 발견 -> 최소한 하나의 공이 있을 수 있음
                ball_count += 1
        elif grassland[i] == '|' and i + 1 < n and grassland[i + 1] == ')':
            # '|)' 형태 발견 -> 최소한 하나의 공이 있을 수 있음
            ball_count += 1
            i += 1  # 이미 찾은 공을 건너뛰기 위해 인덱스 한 칸 더 이동

    print(f'#{tc} {ball_count}')