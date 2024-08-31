# 아니 기차가 부딪히면 파리만 죽는 게 아닐 거 같은데
# 대체 왜 파리는 왜... 그렇게 왔다갔다 하는거고.. 속력은 또 왜이리 빠른 거고..
def fly_distance(D, A, B, F):
    # 두 기차가 충돌할 때까지 걸리는 시간 계산
    time_until_crash = D / (A + B)
    
    # 파리가 이동한 거리 계산
    fly_movement = time_until_crash * F
    
    return fly_movement

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(float, input().split())

    result = fly_distance(D, A, B, F)
    print(f'#{tc} {result:.6f}')