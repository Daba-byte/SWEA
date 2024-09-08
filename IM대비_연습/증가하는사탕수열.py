def increase_candy(A, B, C):
    if A < B < C: # 이미 증가 중
        return 0 # 안먹어두 대
    if C <= 2: # C가 2보다 작거나 같으면
        return -1 # 아무리 먹어두 증가 못해
    if B <= 1: # B도 마찬가지
        return -1
    
    eat_candy = 0 # 너 사탕 얼마나 먹을거야? 백개!!!

    while not (A < B < C):
        if A >= B:
            if B > 1:
                eat_candy += 1
                A -= 1
            else:
                return -1
        if B >= C:
            if C > 2:
                eat_candy += 1
                B -= 1
            else:
                return -1
    return eat_candy # 현실

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    result = increase_candy(A, B, C)
    print(f'#{tc} {result}')