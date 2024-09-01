# 종민아 넌 삼전 갔구나 개부럽다
# 돈도 많이 벌텐데 걍 아무 회사꺼 쓰지
def save_money(P, Q, R, S, W):
    # A 회사 요금
    A_money = P * W
    # B 회사 요금
    if R >= W:
        B_money = Q
    else:
        B_money = Q + (W - R) * S

    # 요금 비교
    return min(A_money, B_money)

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    result = save_money(P, Q, R, S, W)
    print(f'#{tc} {result}')