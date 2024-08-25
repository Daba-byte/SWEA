def bus(K, N, M, charger):
    charge_count = 0
    crr_pos = 0 # 현재 위치

    # 충전소 리스트에서 마지막 충전소까지 차례대로 접근
    while crr_pos + K < N: # 종점까지 반복
        next_pos = crr_pos # 현재 위치에서 시작

        # K 범위 내 가장 먼 충전소 찾기
        for i in range(M): # 충전기 개수만큼
            # 충전소가 현재위치 + 이동 정류장 범위 보다 작거나 같다면
            if charger[i] <= crr_pos + K:
                next_pos = charger[i] # 다음 위치는 충전소
            else: # 충전소가 현재부터 이동 정류장 범위 내에 없으면
                break # 반복 중지
        
        if next_pos == crr_pos: # 반복 중지되어 다음 위치가 현재 위치면
            return 0 # 잘못된 정류장
        
        # 충전하고 이동
        charge_count += 1 # 충전 수 증가
        crr_pos = next_pos # 다음 정류장을 현재 위치로 저장
        
    return charge_count

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    result = bus(K, N, M, charger)
    print(f'#{tc} {result}')