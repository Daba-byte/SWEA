def spray_plus(N, M, arr, x, y):
    total_flies = 0
    # 델타 방향 정의
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌
    
    # 중심의 파리 수
    total_flies += arr[x][y]
    
    # 각 방향으로 M-1 칸만큼 스프레이 적용
    for dx, dy in directions:
        for step in range(1, M):
            nx, ny = x + dx * step, y + dy * step
            if 0 <= nx < N and 0 <= ny < N:
                total_flies += arr[nx][ny]
            else:
                break
    
    return total_flies

def spray_x(N, M, arr, x, y):
    total_flies = 0
    # 델타 방향 정의
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # 하우, 하좌, 상우, 상좌
    
    # 중심의 파리 수
    total_flies += arr[x][y]
    
    # 각 대각선 방향으로 M-1 칸만큼 스프레이 적용
    for dx, dy in directions:
        for step in range(1, M):
            nx, ny = x + dx * step, y + dy * step
            if 0 <= nx < N and 0 <= ny < N:
                total_flies += arr[nx][ny]
            else:
                break
    
    return total_flies

def max_flies(N, M, arr):
    max_flies_caught = 0
    
    for i in range(N):
        for j in range(N):
            # +에서
            flies_plus = spray_plus(N, M, arr, i, j)
            max_flies_caught = max(max_flies_caught, flies_plus)
            
            # x에서
            flies_x = spray_x(N, M, arr, i, j)
            max_flies_caught = max(max_flies_caught, flies_x)
    
    return max_flies_caught

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = max_flies(N, M, arr)
    print(f'#{tc} {result}')

##### 또 풀어보자 #####
def plus_spray(N, M, grid, x, y):
    total_flies = 0
    # 방향: 하, 상, 우, 좌
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    total_flies += grid[x][y] # 가운데 파리다

    # 각 방향으로 M-1칸만큼 스프레이
    for dx, dy in directions:
        for i in range(1, M):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < N and 0 <= ny < N:
                total_flies += grid[nx][ny]
            else:
                break
    return total_flies

def x_spray(N, M, grid, x, y):
    total_flies = 0
    # 방향: 하우, 하좌, 상우, 상좌
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    total_flies += grid[x][y] # 나 가운데야 또 와써

    # 대각선 방향으로 M-1칸만큼 스프레이 뿌릴 거야
    for dx, dy in directions:
        for i in range(1, M):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < N and 0 <= ny < N:
                total_flies += grid[nx][ny]
            else:
                break

    return total_flies

# 파리 넌 진짜 큰일났다
def kill_flies(N, M, grid):
    max_kill_flies = 0

    for x in range(N):
        for y in range(N):
            # +에서
            flies_plus = plus_spray(N, M, grid, x, y)
            max_kill_flies = max(max_kill_flies, flies_plus)
            
            # x에서
            flies_x = x_spray(N, M, grid, x, y)
            max_kill_flies = max(max_kill_flies, flies_x)
    
    return max_kill_flies

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = kill_flies(N, M, grid)
    print(F'#{tc} {result}')