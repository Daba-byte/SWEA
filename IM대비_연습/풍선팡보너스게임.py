def score_calc(N, score_board, i, j):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향

    score = score_board[i][j] # 가운데

    for di, dj in directions:
        for k in range(1, N+1): # 가운데 더했으니까 빼고, 뺀 만큼 더 가고
            ni, nj = i + di * k, j + dj * k
            if 0 <= ni < N and 0 <= nj < N:  # 범위 안일 때
                score += score_board[ni][nj] # 점수 더해

    return score # 점수들

def play_game(N, score_board):
    max_score, min_score = 0, 1000000 # 점수 계산 변수

    for i in range(N):
        for j in range(N):
            score = score_calc(N, score_board, i, j)
            max_score = max(max_score, score) # 첫 판
            min_score = min(min_score, score) # 두번째 판

    return max_score - min_score # 최종 점수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score_board = [list(map(int, input().split())) for _ in range(N)]

    result = play_game(N, score_board)
    print(f'#{tc} {result}')