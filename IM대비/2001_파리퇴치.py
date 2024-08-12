def kill_bug(N, M, arr):
    max_bug = 0
    for i in range(N - M +1):
        for j in range(N - M + 1):
            current_bug = 0
            for x in range(M):
                for y in range(M):
                    current_bug += arr[i + x][j + y]
                     
            if current_bug > max_bug:
                max_bug = current_bug
                 
    return max_bug
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    result = kill_bug(N, M, arr)
    print(f'#{tc} {result}')