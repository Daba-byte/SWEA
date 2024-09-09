def find_max_one(N, num_list):
    max_one = 0
    for i in range(N):
        crr_one = 0
        if num_list[i] == 1:
            for j in range(i, N):
                if num_list[j] == 1:
                    crr_one += 1
                    max_one = max(max_one, crr_one)
                else:
                    crr_one = 0

    return max_one

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().strip()))

    result = find_max_one(N, num_list)
    print(f'#{tc} {result}')