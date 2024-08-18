def cover_area(n, grid):
    # 기지국 타입에 따른 최대 커버 거리 설정
    max_steps = {
        'A': 1,  # 1칸
        'B': 2,  # 2칸
        'C': 3   # 3칸
    }
    
    # 방향 벡터 설정 (동, 서, 남, 북 방향)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래쪽, 왼쪽, 위쪽
    
    # 각 셀이 커버됐는지 여부를 기록하는 배열
    covered = [[False] * n for _ in range(n)]
    
    # 기지국의 위치에서 커버할 영역을 계산
    for i in range(n):
        for j in range(n):
            if grid[i][j] in max_steps:
                station_type = grid[i][j]
                for dx, dy in directions:
                    for step in range(1, max_steps[station_type] + 1):
                        ni, nj = i + dx * step, j + dy * step
                        if 0 <= ni < n and 0 <= nj < n:
                            if grid[ni][nj] == 'H':
                                covered[ni][nj] = True
    
    # 커버되지 않는 집의 수를 계산
    uncovered_count = sum(1 for i in range(n) for j in range(n) if grid[i][j] == 'H' and not covered[i][j])
    
    return uncovered_count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = cover_area(N, arr)
    print(f'#{tc} {result}')