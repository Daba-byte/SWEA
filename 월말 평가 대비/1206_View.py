def view(N, arr):
    view_count = 0

    for i in range(2, N-2):
        # 왼쪽, 오른쪽 두 칸 놑이 중 최대값
        left_max = max(arr[i-2], arr[i-1])
        right_max = max(arr[i+1], arr[i+2])

        max_house = max(left_max, right_max)

        # 현재 건물이 좌우 두칸보다 높으면
        if arr[i] > max_house:
            # 조망권 수 = 현재 건뭉 높이 - 좌우 최대 건물 높이
            view_count += arr[i] - max_house

    return view_count

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = view(N, arr)
    print(f'#{tc} {result}')

#### 2차원 배열 사용 ####
def view(N, arr):
    grid = [[0] * N for _ in range(260)]
    view_count = 0
    # 건물 높이만큼 2차원 배열에 1 생성
    for i in range(N):
        for j in range(arr[i]):
            grid[j][i] = 1

    for i in range(2, N-2):
        for j in range(arr[i]): # 현재 건물 높이만큼만 검사
            if grid[j][i-2] == 0 and grid[j][i-1] == 0 and grid[j][i+1] == 0 and grid[j][i+2] == 0:
                view_count += 1

    return view_count

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = view(N, arr)
    print(f'#{tc} {result}')