def min_paint_cost(N, M, flag):
    # 비용 테이블 초기화
    white_cost = [0] * N
    blue_cost = [0] * N
    red_cost = [0] * N
    
    for i in range(N):
        white_cost[i] = M - flag[i].count('W')
        blue_cost[i] = M - flag[i].count('B')
        red_cost[i] = M - flag[i].count('R')
    
    min_cost = 10000
    
    # 가능한 모든 (i, j) 조합에 대해 최소 비용 계산
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            white_section = sum(white_cost[:i+1])
            blue_section = sum(blue_cost[i+1:j+1])
            red_section = sum(red_cost[j+1:])
            
            total_cost = white_section + blue_section + red_section
            min_cost = min(min_cost, total_cost)
    
    return min_cost

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input().strip() for _ in range(N)]
    
    result = min_paint_cost(N, M, flag)
    print(f"#{t} {result}")