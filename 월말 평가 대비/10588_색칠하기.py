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