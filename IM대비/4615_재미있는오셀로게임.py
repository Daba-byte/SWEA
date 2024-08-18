def flip_discs(board, x, y, color):
    # 돌을 놓고 상대편 돌을 뒤집는 함수
    opponent = 2 if color == 1 else 1  # 상대편 돌 색깔 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 8방향 탐색
    flips = []

    # 8방향에 대해 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        to_flip = []

        # 상대편 돌이 있는 방향으로 이동하며 뒤집을 돌 기록
        while 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == opponent:
            to_flip.append((nx, ny))
            nx += dx
            ny += dy

        # 자신 돌을 만날 경우 뒤집을 돌을 실제로 뒤집음
        if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == color:
            flips.extend(to_flip)

    # 기록한 뒤집을 돌들을 실제로 뒤집음
    for fx, fy in flips:
        board[fx][fy] = color

def play_othello(N, M, moves):
    # 보드 초기화
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    board[mid - 1][mid - 1], board[mid][mid] = 2, 2  # 백돌 초기 배치
    board[mid - 1][mid], board[mid][mid - 1] = 1, 1  # 흑돌 초기 배치

    # 각 돌을 놓는 과정을 처리
    for move in moves:
        x, y, color = move[0] - 1, move[1] - 1, move[2]
        board[x][y] = color  # 돌을 놓음
        flip_discs(board, x, y, color)  # 상대편 돌을 뒤집음

    # 돌 개수 세기
    black, white = 0, 0
    for row in board:
        for cell in row:
            if cell == 1:
                black += 1
            elif cell == 2:
                white += 1

    return black, white

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    moves = [list(map(int, input().split())) for _ in range(M)]

    black, white = play_othello(N, M, moves)
    print(f'#{tc} {black} {white}')