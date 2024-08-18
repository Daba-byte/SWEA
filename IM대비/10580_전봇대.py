T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    wires = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        wires.append((Ai, Bi))
    
    # 교차점 개수 계산
    intersections = 0
    
    # 모든 전선 쌍을 비교하여 교차점 찾기
    for i in range(N):
        for j in range(i + 1, N):
            A1, B1 = wires[i]
            A2, B2 = wires[j]
            
            if (A1 < A2 and B1 > B2) or (A1 > A2 and B1 < B2):
                intersections += 1

    print(f'#{tc} {intersections}')