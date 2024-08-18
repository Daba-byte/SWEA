def quadrangle(N, arr):
    mex_area = 0
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                # 현재 위치(i,j)에서 시작하는 사각형을 찾음
                width = 0
                height = 0
                # 가로 길이 구하기
                while j + width < N and arr[i][j + width] == 1:
                    width += 1
                # 세로길이 구하기
                while i + height < N and arr[i + height][j] == 1:
                    height += 1
                # 사각형 면적 계산
                area = width * height
                if area > mex_area:
                    mex_area = area 

    return mex_area

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = quadrangle(N, arr)
    print(f'#{tc} {result}')