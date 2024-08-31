def square(N, grid):
    min_i, min_j = N, N # '#' 문자가 있는 가장 작은 좌표(왼쪽 위)
    max_i, max_j = -1, -1 # '#' 문자가 있는 가장 큰 좌표(오른쪽 아래)
    # 좌표 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)

    # 정사각형 확인하기
    if (max_i - min_i + 1) != (max_j - min_j + 1):
        return 'no'
    
    # 정사각형 안이 모두 '#'으로 채워져있는지 확인하기
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if grid[i][j] != '#':
                return 'no'
    
    return 'yes'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    result = square(N, grid)
    print(f'#{tc} {result}')