def rotate_90(N, arr):
    # 90도 회전
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]
    return new_arr

def rotate_180(N, arr):
    # 180도 회전
    return rotate_90(N, rotate_90(N, arr))

def rotate_270(N, arr):
    # 270도 회전
    return rotate_90(N, rotate_180(N, arr))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result_90 = rotate_90(N, arr)
    result_180 = rotate_180(N, arr)
    result_270 = rotate_270(N, arr)

    print(f'#{tc}')
    for i in range(N):
        # 각 줄의 3개의 배열을 이어붙여서 출력
        line_90 = ''.join(map(str, result_90[i]))
        line_180 = ''.join(map(str, result_180[i]))
        line_270 = ''.join(map(str, result_270[i]))
        print(line_90, line_180, line_270)