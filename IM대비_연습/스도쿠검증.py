def sudoku_judgment(grid):
    for i in range(9): # 가로
            if len(set(grid[i])) != 9:
                return 0

    for j in range(9): # 세로
        col = [grid[i][j] for i in range(9)]
        if len(set(col)) != 9:
            return 0

    for x in range(0, 9, 3): # 박스
        for y in range(0, 9, 3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(grid[x+i][y+j])
            if len(set(box)) != 9:
                return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku_judgment(grid)
    print(f'#{tc} {result}')