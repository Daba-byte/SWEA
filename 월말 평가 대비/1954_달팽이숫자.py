def snail(N):
    grid = [[0] * N for _ in range(N)]
    # 하 델타 못 쓰겠는데 문제 안나오면 좋겠다
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0 # 시작 위치
    direc = 0 # 오른쪽
    num = 1 # 채울 숫자

    for _ in range(N *N): # N*N 칸에 숫자 채우기
        grid[x][y] = num
        num += 1
        # 다음 위치 계산
        nx, ny = x + dx[direc], y + dy[direc]
        # 경계 벗어나거나 칸에 이미 숫자가 있으면
        if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] != 0:
            direc = (direc + 1) % 4 # 방향 전환
            nx, ny = x + dx[direc], y + dy[direc]

        x, y = nx, ny

    return grid  

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    result = snail(N)
    print(f'#{tc}')
    # 결과 출력 개같이 하네 진짜
    # 화내지마 다빈아 진정해
    for row in result:
        print(' '.join(map(str, row)))