# 나 파리퇴치 일억번 풀었다 이제 파리퇴치 개고수됨 ㅋㅋ
def spray_plus(N, M, flies, i, j):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    total_flies = flies[i][j]

    for di, dj in directions:
        for k in range(1, M):
            ni, nj = i + di * k, j + dj * k
            if 0 <= ni < N and 0 <= nj < N:
                total_flies += flies[ni][nj]

    return total_flies

def spray_X(N, M, flies, i, j):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    total_flies = flies[i][j]

    for di, dj in directions:
        for k in range(1, M):
            ni, nj = i + di * k, j + dj * k
            if 0 <= ni < N and 0 <= nj < N:
                total_flies += flies[ni][nj]

    return total_flies

def kill_flies(N, M, flies):
    max_flies = 0

    for i in range(N):
        for j in range(N):
            plus_flies = spray_plus(N, M, flies, i, j)
            x_flies = spray_X(N, M, flies, i, j)
            max_flies = max(max_flies, plus_flies, x_flies)

    return max_flies

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    result = kill_flies(N, M, flies)
    print(f'#{tc} {result}')