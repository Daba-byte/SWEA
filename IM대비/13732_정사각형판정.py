def square(N, arr):
    min_i, min_j = N, N
    max_i, max_j = -1, -1

    # 모든 '#' 문자의 좌표를 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if i < min_i: min_i = i
                if i > max_i: max_i = i
                if j < min_j: min_j = j
                if j > max_j: max_j = j

    # 찾은 좌표들이 정사각형을 이루는지 확인
    side_length = max(max_i - min_i + 1, max_j - min_j + 1)
    for i in range(min_i, min_i + side_length):
        for j in range(min_j, min_j + side_length):
            if i >= N or j >= N or arr[i][j] != '#':
                return 'no'
    
    return 'yes'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = square(N, arr)
    print(f'#{tc} {result}')