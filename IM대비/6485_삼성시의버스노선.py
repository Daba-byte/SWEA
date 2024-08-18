def process_case(N, routes, P, queries):
    # 각 버스 정류장 번호에 대해 몇 개의 버스 노선이 지나는지를 기록할 배열 초기화
    bus_count = [0] * 5001  # 1부터 5000까지의 정류장 번호를 다루기 위해 5001 크기의 배열 사용
    
    # 각 버스 노선에 대해 처리
    for Ai, Bi in routes:
        for stop in range(Ai, Bi + 1):
            bus_count[stop] += 1  # 범위 내의 정류장 번호에 대해 버스 노선의 개수를 증가시킴
    
    # 주어진 쿼리에 대해 결과 생성
    result = [str(bus_count[Cj]) for Cj in queries]  # 각 정류장 번호에 대해 버스 노선의 개수를 문자열로 변환
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    routes = []
    for _ in range(N):
        # 버스 노선의 범위를 읽어옴
        Ai, Bi = map(int, input().strip().split())
        routes.append((Ai, Bi))
    
    P = int(input())
    queries = []
    for _ in range(P):
        # 쿼리로 주어진 버스 정류장 번호를 읽어옴
        Cj = int(input().strip())
        queries.append(Cj)
    
    # 현재 테스트 케이스를 처리
    result = process_case(N, routes, P, queries)
    # 결과를 형식에 맞게 출력
    print(f'#{tc} {" ".join(result)}')