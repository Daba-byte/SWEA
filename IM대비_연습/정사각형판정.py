def square_judgment(N, board): # 정사강형 판정
    # 좌표 찾기 위한 변수 할당
    min_i, min_j = N, N
    max_i, max_j = -1, -1
    
    # '#'이 있는 구간의 좌표를 찾어.
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)

    # 길이 비교해서 정사각형인지 확인
    if (max_i - min_i) != (max_j - min_j):
        return 'no'

    # 사각형 안이 채워져 있는지 확인    
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if board[i][j] != '#':
                return 'no'
            
    # 다 확인하면 정사각형 맞음
    return 'yes'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    result = square_judgment(N, board)
    print(f'#{tc} {result}')