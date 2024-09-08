def omock_count(N, board, i, j): # 오목 세는 구양
    # 오목 판정은 8방향으로 할 수 있지만, 보드 전체를 순회할 것이기 때문에 각 방향 당 한쪽씩만 보면 됨
    directions = [(0, 1), (1, 1), (1, 0), (-1, 1)] # 방향인구양

    if board[i][j] != 'o': # 바둑알 아니면
        return 0 # 바로 반환

    for di, dj in directions: # 방향 가져와
        cnt = 1 # 본인부터 개수 시작
        for k in range(1, 5): # 나는 카운트 올렸으니까 그 다음 꺼 부터
            ni, nj = i + di * k, j + dj * k # 좌표 설정 하고
            if 0 <= ni < N and 0 <= nj < N: # 보드판 안에서
                if board[ni][nj] == 'o': # 다음 좌표가 바둑알이 맞으면
                    cnt += 1 # 카운트 올려
                else: # 아니면
                    break # 멈춰
            if cnt == 5: # 카운트 5일 때만
                return 1 # 오목이야
            
    return 0 # 아니면 육목이상임

def omock_judgment(N, board):
    for i in range(N):
        for j in range(N):
            if omock_count(N, board, i, j):
                return 'YES' # 축하해 넌 오목이야
            
    return 'NO' # 넌 오목이 아니야

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    result = omock_judgment(N, board)
    print(f'#{tc} {result}')