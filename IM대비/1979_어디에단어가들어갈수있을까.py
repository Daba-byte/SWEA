def where_word(N, K, arr):
    word_count = 0
    # 가로 방향 검사
    for i in range(N):
        consecutive = 0
        for j in range(N):
            if arr[i][j] ==1:
                consecutive += 1
            else:
                if consecutive == K:
                    word_count += 1
                consecutive = 0
        if consecutive == K:
            word_count += 1
             
    # 세로 방향 검사
    for j in range(N):
        consecutive = 0
        for i in range(N):
            if arr[i][j] == 1:
                consecutive += 1
            else:
                if consecutive == K:
                    word_count += 1
                consecutive = 0
        if consecutive == K:
            word_count += 1
             
    return word_count
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    result = where_word(N, K, arr)
    print(f'#{tc} {result}')

###### 간단...한가..? #######
def where_word(N, K, arr):
    word_count = 0
    
    for i in range(N):
        row_consecutive = 0
        col_consecutive = 0
        for j in range(N):
            # 가로 방향 검사
            if arr[i][j] == 1:
                row_consecutive += 1
            else:
                if row_consecutive == K:
                    word_count += 1
                row_consecutive = 0
            
            # 세로 방향 검사
            if arr[j][i] == 1:
                col_consecutive += 1
            else:
                if col_consecutive == K:
                    word_count += 1
                col_consecutive = 0
        
        # 각 행/열의 끝에서 확인
        if row_consecutive == K:
            word_count += 1
        if col_consecutive == K:
            word_count += 1

    return word_count

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = where_word(N, K, arr)
    print(f'#{tc} {result}')