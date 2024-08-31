def jeom(N):
    cnt = 0 # 격자점 수

    # 0,0으로부터 반지름 길이까지 안에 범위의 모든 쌍을 검사
    for i in range(-N, N+1):
        for y in range(-N, N+1):
            # 원 안에 포함되는지 확인
            if i**2 + y**2 <= N**2:
                cnt += 1
    
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = jeom(N)
    print(f'#{tc} {result}')

#######
# 문제가 이해가 안되냐 아놔
# 격자점은 x와 y 좌표가 모두 정수인 점을 의미함
# 주어진 원의 중심은 (0,0)이고, 반지름이 N
# 원의 방정식: i**2 + y**2 <= N**2
# 이 식은 원의 중심에서부터 반지름이 N인 원의 내부와 경계에 해당하는 점들을 나타냄.