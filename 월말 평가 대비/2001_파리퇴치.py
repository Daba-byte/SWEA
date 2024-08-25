def pari(N, M, grid):
    max_pari = 0
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_pari = 0
            for x in range(M):
                for y in range(M):
                    kill_pari += grid[i+x][j+y]

            max_pari = max(max_pari, kill_pari)

    return max_pari

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = pari(N, M, grid)
    print(f'#{tc} {result}')