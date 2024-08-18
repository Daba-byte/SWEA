def find_longest_structure(n, m, grid):
    max_length = 0
    
    # 행을 순회하며 최대 길이 찾기
    for i in range(n):
        current_length = 0
        for j in range(m):
            if grid[i][j] == 1:
                current_length += 1
            else:
                if current_length >= 2:  # 1x1은 노이즈이므로 최소 길이가 2 이상일 때만 고려
                    max_length = max(max_length, current_length)
                current_length = 0
        if current_length >= 2:  # 행의 마지막이 연속된 '1'로 끝나는 경우
            max_length = max(max_length, current_length)
    
    # 열을 순회하며 최대 길이 찾기
    for j in range(m):
        current_length = 0
        for i in range(n):
            if grid[i][j] == 1:
                current_length += 1
            else:
                if current_length >= 2:
                    max_length = max(max_length, current_length)
                current_length = 0
        if current_length >= 2:  # 열의 마지막이 연속된 '1'로 끝나는 경우
            max_length = max(max_length, current_length)
    
    return max_length

# 입력 처리
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    result = find_longest_structure(N, M, grid)
    print(f'#{test_case} {result}')