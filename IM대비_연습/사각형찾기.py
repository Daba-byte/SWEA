def find_square(N, grid): # 사각형을 찾자
    max_area, crr_area = 0, 0 # 영역을 구할 거니까

    for i in range(N): # 일단 돌아
        for j in range(N): # 돌아 돌아
            if grid[i][j] == 1: # 1이면? 어라 사각형 시작
                width_count = 0 # 일단 초기화
                height_count = 0 # 너두
                
                for k in range(i, N): # 가로 셀거야
                    if grid[k][j] == 1: # 너 사각형이야?
                        width_count += 1 # 그럼 카운트 올려
                    else: # 아니면
                        break # 멈춰
                
                for l in range(j, N): # 세로는?
                    if grid[i][l] == 1: # 너 사각형 맞냐고 이 자식아
                        height_count += 1 # 맞아요 ㅠㅠ
                    else: # 아니면
                        break # 멈처!
                
                crr_area = width_count * height_count # 영역 계산 갈겨
                max_area = max(max_area, crr_area) # 젤 큰놈 나와
        
    return max_area # 저에요

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = find_square(N, grid)
    print(f'#{tc} {result}')