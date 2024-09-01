# 난 사탕보다 초콜릿이 좋은뎅
def candy_yummy(A, B, C):
    if A < B < C: # 이미 만족
        return 0 # 바로 반환
    
    if C <= 2: # C가 2 이하면
        return -1 # 순증가 불가

    eat_candy = 0 # 얼마나 먹을거야
    
    while not (A < B < C): # 순증가 만족까지
        if B <= A: # B가 A보다 작거나 같으면
            if B > 1: # B가 1보다 큰 경우에만 먹어야 함
                eat_candy += 1 # 사탕 하나 냠냠
                A -= 1 # A상자에서 먹어
            else:
                return -1
        if C <= B: # C가 B보다 작거나 같으면
            if C > 2: # C가 2보다 커야함
                eat_candy += 1 # 사탕 냠냠
                B -= 1 # B상자에서 먹어
            else:
                return -1
    
    return eat_candy # 이만큼 머거따

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    result = candy_yummy(A, B, C)
    print(f'#{tc} {result}')