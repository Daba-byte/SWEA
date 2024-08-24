T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 최대, 최소 설정
    min_num = 100000000
    max_num = -100000000

    # 첫 번째 인덱스부터 N-M까지
    for i in range(N - M + 1):
        # i번째 인덱스부터 i+M-1까지 구간합
        crr_sum = sum(ai[i:i + M])
        if max_num < crr_sum:
            max_num = crr_sum
        if min_num > crr_sum:
            min_num = crr_sum

    print(f'#{tc} {max_num - min_num}')