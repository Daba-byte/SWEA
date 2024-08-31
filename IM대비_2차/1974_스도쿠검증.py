def sudoku(grid):
    # 가로 검증
    for i in range(9):
        if len(set(grid[i])) != 9: # 중복 제거시 길이가 9가 아니면
            return 0 # 넌 스도쿠가 아니야
    # 세로 검증
    for j in range(9):
        col = [grid[i][j] for i in range(9)] # 세로
        if len(set(col)) != 9: # 중복 있니?
            return 0 # 그럼 너도 함께 갈 수 없어
    # 3*3 검증
    for x in range(0, 9, 3): # 0부터 9까지 3칸씩 검사
        for y in range(0, 9, 3):
            box = [] # 3*3 박스 검증할 리스트
            for i in range(3): # 한번 보자
                for j in range(3): # 돌면서
                    box.append(grid[x+i][y+j]) # 넣기
            if len(set(box)) != 9: # 너도 중복 있으면
                return 0 # 안돼
            
    return 1 # 축하해 넌 스도쿠야

T = int(input())
for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku(grid)
    print(f'#{tc} {result}')