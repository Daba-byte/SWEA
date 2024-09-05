def section_sum(N, M, ai):
    min_number = 10000000000
    max_number = -10000000000
    for i in range(N - M + 1):
        crr_sum = sum(ai[i:i + M])
        max_number = max(max_number, crr_sum)
        min_number = min(min_number, crr_sum)

    return max_number - min_number

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    result = section_sum(N, M, ai)
    print(f'#{tc} {result}')