def has_five_in_a_row(board, N):
    def check_line(r, c, dr, dc):
        """ r, c: 시작 위치, dr, dc: 방향 벡터 """
        count = 0
        while 0 <= r < N and 0 <= c < N:
            if board[r][c] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
            r += dr
            c += dc
        return False

    # 가로와 세로 검사
    for i in range(N):
        if check_line(i, 0, 0, 1):  # 가로 검사
            return True
        if check_line(0, i, 1, 0):  # 세로 검사
            return True

    # 대각선 검사 (왼쪽 위에서 오른쪽 아래)
    for i in range(N):
        if check_line(i, 0, 1, 1):  # 왼쪽 위에서 오른쪽 아래
            return True
        if check_line(0, i, 1, 1):  # 대각선 시작 위치 조정
            return True

    # 대각선 검사 (왼쪽 아래에서 오른쪽 위)
    for i in range(N):
        if check_line(i, 0, -1, 1):  # 왼쪽 아래에서 오른쪽 위
            return True
        if check_line(N-1, i, -1, 1):  # 대각선 시작 위치 조정
            return True

    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    if has_five_in_a_row(arr, N):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')


##### 두번째 풀이 ######

def omok(N, board):
    # 가로 검사
    for row in board:
        count = 0
        for cell in row:
            if cell == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0

    # 세로 검사
    for col in range(N):
        count = 0
        for row in range(N):
            if board[row][col] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0

    # 대각선 검사 (왼쪽 위에서 오른쪽 아래)
    for start_row in range(N):
        count = 0
        r, c = start_row, 0
        while r < N and c < N:
            if board[r][c] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
            r += 1
            c += 1

    for start_col in range(1, N):
        count = 0
        r, c = 0, start_col
        while r < N and c < N:
            if board[r][c] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
            r += 1
            c += 1

    # 대각선 검사 (왼쪽 아래에서 오른쪽 위)
    for start_row in range(N):
        count = 0
        r, c = start_row, 0
        while r >= 0 and c < N:
            if board[r][c] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
            r -= 1
            c += 1

    for start_col in range(1, N):
        count = 0
        r, c = N - 1, start_col
        while r >= 0 and c < N:
            if board[r][c] == 'o':
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
            r -= 1
            c += 1

    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    result = []
    if omok(N, arr):
        result.append('YES')
    else:
        result.append('NO')
    print(f'#{tc} {" ".join(result)}')