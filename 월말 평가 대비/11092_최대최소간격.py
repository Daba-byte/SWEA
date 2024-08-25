def hing(N, arr):
    max_num = -1000
    min_num =1000

    max_idx = -1
    min_idx = -1

    for i in range(N):
        if min_num > arr[i]:
            min_num = arr[i]
            min_idx = i
        if max_num <= arr[i]: # 같은 숫자면 가장 마지막 위치
            max_num = arr[i]
            max_idx = i

    return abs(max_idx - min_idx)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = hing(N, arr)
    print(f'#{tc} {result}')