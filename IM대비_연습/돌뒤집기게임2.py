def turn_stones(N, stones, i, j):
    center = i - 1
    for k in range(1, j +1):
        left = center - k
        right = center + k 

        if left < 0 or right >= N:
            break

        if stones[left] == stones[right]:
            stones[left] = 1 - stones[left]
            stones[right] = 1 - stones[right]

    return ' '.join(map(str, stones))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        result = turn_stones(N, stones, i, j)
    print(f'#{tc} {result}')