def balloon_pang(N, M ,balloon):
    
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    ans = []
    
    for i in range(N):
        for j in range(M):
            sum_ggotraru = balloon[i][j]
            for x in range(4):
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_ggotraru += balloon[ni][nj]
                    ans.append(sum_ggotraru)

    return max(ans)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    result = balloon_pang(N, M, balloon)
    print(f'#{tc} {result}')