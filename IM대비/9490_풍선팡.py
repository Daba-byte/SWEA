# 자꾸 하나씩만 터지고 가운데 숫자만큼 터뜨리는 법을 몰랐음
def balloon(N, M, arr):
    # 방향 벡터: 아래, 오른쪽, 위, 왼쪽
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    
    max_score = 0
    for i in range(N):
        for j in range(M):
            sum_score = arr[i][j]  # 현재 위치의 점수
            for k in range(4): # k는 방향. 0 = 아래, 1= 오른쪽, 2 = 위, 3 = 왼쪽
                for step in range(1, arr[i][j] + 1):
                    ni, nj = i + di[k] * step, j + dj[k] * step # 새로운 위치 계산
                    if 0 <= ni < N and 0 <= nj < M: # 배열 안에 있다면
                        sum_score += arr[ni][nj]
            if sum_score > max_score:
                max_score = sum_score
    
    return max_score

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = balloon(N, M, arr)
    print(f'#{tc} {result}')