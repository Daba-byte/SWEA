def is_valid_sudoku(arr):
    def is_valid_block(block):
        # 중복을 제거하기 위해 set 사용
        block = [num for num in block if num != 0]  # 0은 무시 (빈 칸)
        return len(block) == len(set(block))
 
    # 행 검사
    for row in arr:
        if not is_valid_block(row):
            return 0
 
    # 열 검사
    for col in range(9):
        if not is_valid_block([arr[row][col] for row in range(9)]):
            return 0
 
    # 3x3 서브그리드 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [arr[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_block(block):
                return 0
 
    return 1
 
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = is_valid_sudoku(arr)
    print(f'#{tc} {result}')


########################################################
# 더럽게 풀어봄

# def sudoku(arr):
#     # 행 검사
#     for i in range(9):
#         row_check = [0] * 10  # 숫자 1~9의 중복을 확인하기 위한 배열
#         for j in range(9):
#             num = arr[i][j]
#             if num != 0:  # 0은 빈 칸이므로 무시
#                 if row_check[num] == 1:
#                     return 0
#                 row_check[num] = 1
 
#     # 열 검사
#     for j in range(9):
#         col_check = [0] * 10
#         for i in range(9):
#             num = arr[i][j]
#             if num != 0:
#                 if col_check[num] == 1:
#                     return 0
#                 col_check[num] = 1
 
#     # 3x3 서브그리드 검사
#     for x in range(0, 9, 3):
#         for y in range(0, 9, 3):
#             grid_check = [0] * 10
#             for i in range(3):
#                 for j in range(3):
#                     num = arr[x + i][y + j]
#                     if num != 0:
#                         if grid_check[num] == 1:
#                             return 0
#                         grid_check[num] = 1
 
#     return 1
 
# T = int(input())
# for tc in range(1, T + 1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
 
#     result = sudoku(arr)
#     print(f'#{tc} {result}')