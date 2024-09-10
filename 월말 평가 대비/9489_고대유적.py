def find_temp(N, M, grid): # 고대 유적을 찾자
    big_temp = 0 # 젤 긴 거

    for i in range(N): # 열 돌면서
        width = 0 # 젤 긴 유적은
        for j in range(M):
            if grid[i][j] == 1: # 1 만나면
                width += 1 # 카운트 올려
            else: # 아니면
                if width >= 2: # 노이즈가 아닐 때
                    big_temp = max(big_temp, width) # 젤 큰 거 갱신
                width = 0 # 다시 0
        if width >= 2: # 다 돌고 노이즈가 아닐 때
            big_temp = max(big_temp, width) # 한 번 더 갱신

    for j in range(M): # 행이랑
        height = 0 # 열만 바꾸고
        for i in range(N): # 다 똑같음
            if grid[i][j] == 1:
                height += 1
            else:
                if height >= 2:
                    big_temp = max(big_temp, height)
                height = 0
        if height >= 2:
            big_temp = max(big_temp, height)
    
    return big_temp # 반환

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = find_temp(N, M, grid)
    print(f'#{tc} {result}')