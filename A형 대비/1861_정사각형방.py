def find_room(N, room_numbers):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            for K in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    break

    cnt = max_cnt = start = 0
    # 어우 졸라 어렵네
    




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room_numbers = [list(map(int, input().split()))]

    result = find_room(N, room_numbers)
    print(f'#{tc} {result}')