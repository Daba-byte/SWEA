def min_max(N, ai):
    max_num = -1000000
    min_num = 100000
    max_inx, min_inx = -1, -1
    for i in range(N):
        if ai[i] >= max_num:
            max_num = ai[i]
            max_inx = i
        if ai[i] < min_num:
            min_num = ai[i]
            min_inx = i
    return abs(max_inx - min_inx)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    result = min_max(N, ai)
    print(f'#{tc} {result}')