T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_num = 100000000
    max_num = -100000000

    for i in range(N):
        if min_num > ai[i]:
            min_num = ai[i]
        if max_num < ai[i]:
            max_num = ai[i]

    print(f'#{tc} {max_num - min_num}')