for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    r_max, c_max, cr_1, cr_2 = 0, 0, 0, 0
    
    # 행, 열, 대각선의 합 계산
    for i in range(100):
        temp_r_max, temp_c_max = 0, 0
        for j in range(100):
            temp_r_max += arr[i][j]  # i번째 행의 합
            temp_c_max += arr[j][i]  # i번째 열의 합
            if i == j:
                cr_1 += arr[i][j]    # 첫 번째 대각선의 합
            if i + j == 99:
                cr_2 += arr[i][j]    # 두 번째 대각선의 합
                
        # 각 행과 열에서의 최대값 갱신
        r_max = max(r_max, temp_r_max)
        c_max = max(c_max, temp_c_max)
 
    result = max(r_max, c_max, cr_1, cr_2)
    print(f'#{tc} {result}') 