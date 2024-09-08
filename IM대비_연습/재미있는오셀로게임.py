# 이게 IN이라니... IM이라니....! 나 머리에 쥐나 못해 이거 A형이야
def flip_discs(N, board, c, r, color): # 뒤집을 거야
    # 색에 맞게 상대 돌 설정
    if color == 1:
        opponent = 2
    else:
        opponent = 1

    # 이건 8방향 다 탐색해야함. 왜인지 묻지마삼. 그냥 나 힘들다. 주석 다는 지금 11시다.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    flips = [] # 뒤집을 좌표 담을 거임

    for dx, dy in directions: # 지겨워 방향 설정
        nx, ny = c + dx, r + dy # 새 좌표야 하나씩 확인할 거라 더하기만 일단 해
        to_flip = [] # 모아서 뒤집을 거니까 하나 더 만들어

        # 범위 안이고 상대돌이면 계속 탐색할 거임
        while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == opponent:
            to_flip.append((nx, ny)) # 상대돌 좌표 넣어
            nx += dx # 다음 돌을
            ny += dy # 봐야 해

        # 우리 돌 만나면
        if 0 <= nx < N and 0 <= ny < N: # 범위 안이네
            if board[nx][ny] == color: # 어라 내 돌이다
                flips.extend(to_flip) # 플립으로 좌표 싹 보내봐라 append 말고 extend 써야 함

    for fx, fy in flips: # 모은 좌표들 돌면서
        board[fx][fy] = color # 넌 이제 다 내돌이야 임마

def otello_game(N, board, r, c, color): # 보드판 초기화 안되게 함수 하나 더 만듬
    r -= 1 # 일단
    c -= 1 # 하나씩 빼 0부터니까
    board[c][r] = color # 내 돌 놓기
    flip_discs(N, board, c, r, color) # 놓고 뒤집어버려


def play_othello(N, moves): # 황다빈 함수에 미쳐있다
    board = [[0] * N for _ in range(N)] # 보드 설정

    # 어우 그냥 다음부터 mid = N//2 하자 길어지니까 보기 싫어
    board[(N//2) - 1][(N//2) - 1], board[(N//2)][(N//2)] = 2, 2
    board[(N//2) - 1][(N//2)], board[(N//2)][(N//2) - 1] = 1, 1

    # 야 움직일 애들 다 나와
    for r, c, color in moves: # 네
        otello_game(N, board, r, c, color) # 게임 시작해

    # 자 이제 게임 끝났어 결과 내놔
    black, white = 0, 0 # 니네 몇개씩 있냐 이거지

    for row in board: # 보드 돌아
        for stone in row: # 돌 꺼내
            if stone == 1: # 검정이니?
                black += 1 # 네
            elif stone == 2: # 하양이니?
                white += 1 # 네네
            # else 썼다가 빈 보드판이 남아있는 경우(stone == 0)까지 세버림 주의하삼

    return black, white # 짠 이게 저희에요

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    moves = [list(map(int, input().split())) for _ in range(M)]

    black, white = play_othello(N, moves)
    print(f'#{tc} {black} {white}')