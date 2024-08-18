def total_distance(N, M, carrots):
    distance = 0
    carry = 0
    
    for i in range(N):
        while carrots[i] > 0:
            # 수레에 실을 수 있는 만큼 실기
            load = min(carrots[i], M - carry)
            carry += load
            carrots[i] -= load
            
            # 수레가 가득 차면 0번 구역으로 돌아가서 비우기
            if carry == M:
                distance += (i + 1) * 2
                carry = 0
        
        # 다음 구역으로 이동
        if i < N - 1:
            carrots[i + 1] += carrots[i]
            distance += 1
    
    # 수레에 남아 있는 당근이 있으면 마지막으로 0번 구역으로 돌아가기
    if carry > 0:
        distance += N
    
    return distance + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    carrots = list(map(int, input().split()))

    result = total_distance(N, M, carrots)
    print(f'#{tc} {result}')