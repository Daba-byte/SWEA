def water_fee(P, Q, R, S, W):
    A_fee = P * W # A회사 요금 리터당 P
    if W >= R: # 기본요금 이상 쓰면
        B_fee = Q + ((W - R) * S) # B회사 요금
    else: # 아니면
        B_fee = Q # 기본 요금
    
    return min(A_fee, B_fee) # 더 작은 건?

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    result = water_fee(P, Q, R, S, W)
    print(f'#{tc} {result}')