def tile_robot(commands):
    wall = [[0] * 10 for _ in range(10)] # 벽이야

    tile_count = 0 # 타일 몇 개 붙일 거야

    for command in commands: # 명령 드루와
        r1, c1, r2, c2 = command # 자
        for i in range(r1, r2+1): # 명령
            for j in range(c1, c2+1): # 이 범위 안에서
                if wall[i][j] == 0: # 타일 없으면
                    wall[i][j] = 1 # 붙이고
                    tile_count += 1 # 카운트 올려

    return tile_count # 이만큼 붙였다 뭐!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    commands = []
    for _ in range(N):
        r1, c1, r2, c2 = map(int, input().split())
        commands.append((r1, c1, r2, c2))

    result = tile_robot(commands)
    print(f'#{tc} {result}')