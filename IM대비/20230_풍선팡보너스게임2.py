def calculate_max_score(n, grid):
    max_score = 0  # 최대 점수를 저장할 변수
    
    for i in range(n):
        for j in range(n):
            current_score = 0
                
            # 같은 행의 모든 점수 합산
            for k in range(n):
                current_score += grid[i][k]
                
            # 같은 열의 모든 점수 합산
            for k in range(n):
                if k != i:  # 이미 더한 행을 중복해서 더하지 않도록 한다
                    current_score += grid[k][j]
                
            # 최대 점수 갱신
            max_score = max(max_score, current_score)
    
    return max_score

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    result = calculate_max_score(N, grid)
    print(f"#{test_case} {result}")