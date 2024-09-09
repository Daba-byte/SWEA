def find_ancient_ruins(N, M, ancient_ruins):
    max_length = 0
    for i in range(N):
        for j in range(M):
            crr_length, crr_length2 = 0, 0
            if ancient_ruins[i][j] == 1:
                for k in range(i, N):
                    if ancient_ruins[k][j] == 1:
                        crr_length += 1
                        max_length = max(max_length, crr_length, crr_length2)
                    else:
                        crr_length = 0
                for l in range(j, M):
                    if ancient_ruins[i][l] == 1:
                        crr_length2 += 1
                        max_length = max(max_length, crr_length, crr_length2)
                    else:
                        crr_length2 = 0

    if max_length <= 1:
        return 0

    return max_length

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ancient_ruins = [list(map(int, input().split())) for _ in range(N)]

    result = find_ancient_ruins(N, M, ancient_ruins)
    print(f'#{tc} {result}')