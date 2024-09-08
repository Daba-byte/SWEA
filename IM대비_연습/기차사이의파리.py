# 거속시만 알면 이지하게 풀림
def crash_train_in_fly(distance, train_A, train_B, fly):
    crash_train_time = distance / (train_A + train_B)

    fly_movement = crash_train_time * fly

    return fly_movement

T = int(input())
for tc in range(1, T+1):
    distance, train_A, train_B, fly = map(int, input(). split())

    result = crash_train_in_fly(distance, train_A, train_B, fly)
    print(f'#{tc} {result}')