def find_purple(areas):
    grid = [[0] * 10 for _ in range(10)]
    count_purple = 0

    # 각 색칠 영역을 처리
    for area in areas:
        r1, c1, r2, c2, color = area
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] == 0:  # 아직 칠해지지 않은 경우
                    grid[i][j] = color
                elif grid[i][j] == 1 and color == 2:  # 빨간색 위에 파란색을 칠할 때
                    grid[i][j] = 3  # 보라색
                    count_purple += 1
                elif grid[i][j] == 2 and color == 1:  # 파란색 위에 빨간색을 칠할 때
                    grid[i][j] = 3  # 보라색
                    count_purple += 1

    return count_purple

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    areas = []
    for _ in range(N):
        # 영역 정보를 입력받아 리스트에 저장
        r1, c1, r2, c2, color = map(int, input().split())
        areas.append((r1, c1, r2, c2, color))
 
    result = find_purple(areas)
    print(f'#{tc} {result}')

##### 풀어보자 #####
# 보라색 칠하기~~
def find_purple(areas):
    grid = [[0] * 10 for _ in range(10)] # 색칠할구양
    count_purple = 0 # 보라색 개수

    for area in areas:
        r1, c1, r2, c2, color = area
        for i in range(r1, r2 + 1): # 가로 영역에서 부터
            for j in range(c1, c2 + 1): # 세로 영역에서 까지
                if grid[i][j] == 0: # 색칠 안되어 있으면
                    grid[i][j] = color # 컬러로 칠해
                elif grid[i][j] == 1 and color == 2: # 1로 칠해져 있고 컬러가 2면
                    grid[i][j] = 3 # 보라색으로 칠해
                    count_purple += 1 # 그만큼 보라색 수가 올라가는 구양
                elif grid[i][j] == 2 and color == 1: # 2로 칠해져 있고 컬러가 3이면
                    grid[i][j] = 3 # 그것도 보라색
                    count_purple += 1 # 이것도 보라색 수 올라가는 구양

    return count_purple # 총 보라색 얼마게!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    areas = []
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        areas.append(r1, c1, r2, c2, color)

    result = find_purple(areas)
    print(f'#{tc} {result}')