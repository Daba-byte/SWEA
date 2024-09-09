def where_word(N, K, grid):
    word_count = 0
 
    #가로
    for i in range(N):
        width = 0
        for j in range(N):
            if grid[i][j] == 1:
                width += 1
            else:
                if width == K:
                    word_count += 1
                width = 0
        if grid[i][N-1] == 1:
            if width == K:
                word_count += 1
 
    # 세로
    for j in range(N):
        height = 0
        for i in range(N):
            if grid[i][j] == 1:
                height += 1
            else:
                if height == K:
                    word_count += 1
                height = 0
        if grid[N-1][j] == 1:
            if height == K:
                word_count += 1
 
    return word_count
 
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
 
    result = where_word(N, K, grid)
    print(f'#{tc} {result}')