T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 돌의 수, 뒤집기 횟수
    stones = list(map(int, input().split()))  # 돌의 초기 상태
    
    for _ in range(M):
        i, j = map(int, input().split())  # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
        
        # 중심돌의 위치
        center = i - 1
        
        # 좌우로 j개의 돌에 대해 처리
        for offset in range(1, j + 1):
            left = center - offset
            right = center + offset
            
            # 범위를 벗어나면 중지
            if left < 0 or right >= N:
                break
            
            # left와 right의 돌이 같은 색이면 뒤집음
            if stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]

    # 결과 출력
    print(f'#{tc} {" ".join(map(str, stones))}')

##### 함수를 쓰자  ######
def turn_stones(N, stones, i, j):
    center = i - 1 # 안녕 나는 중심돌이야
        
    # 좌우로 j개의 돌에 대해 처리
    for offset in range(1, j + 1):
        left = center - offset
        right = center + offset
            
        # 범위를 벗어나면 중지
        if left < 0 or right >= N:
            break
            
        # left와 right의 돌이 같은 색이면 뒤집음
        if stones[left] == stones[right]:
            stones[left] = 1 - stones[left]
            stones[right] = 1 - stones[right]
        

    return " ".join(map(str, stones))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        result = turn_stones(N, stones, i, j)
    print(f'#{tc} {result}')