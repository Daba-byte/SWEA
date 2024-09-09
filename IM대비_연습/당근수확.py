def carrots_moving(N, M, carrots):
    woker_movemant = 0 # 일꾼 이동거리
    capacity = 0 # 담을 양

    for i in range(N):
        while carrots[i] > 0:
            load = min(carrots[i], M - capacity)
            capacity += load
            carrots[i] -= load

            if capacity == M:
                woker_movemant += (i + 1) * 2
                capacity = 0

            # 만약 용량이 다 차지 않았는데 길이 끝나면
            elif capacity < M and carrots[i] == carrots[N-1]:
                woker_movemant += (i + 1) * 2

            elif capacity > M and carrots[i] < M:
                carrots[i+1] += carrots[i] - (M - capacity)
                woker_movemant += (i + 1) * 2
                capacity = 0

    return woker_movemant

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    carrots = list(map(int, input().split()))

    result = carrots_moving(N, M, carrots)
    print(f'#{tc} {result}')