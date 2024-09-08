def carrots_boxing(N, carrots):
    carrots.sort() # 오름차순으로 일단 깔쌈하게 정렬하고
    
    carrots_diff = 10000 # 최소 차이를 구하기 위한 변수

    # 1차원 배열에 이중포문이라니?
    # 실은 구간을 3개로 나누기 위한 거였지롱
    for i in range(1, N-1): # 마지막 구간에 하나는 있어야 하니까
        for j in range(i+1, N): # 두번째 구간부터니까
            small_box = carrots[:i] # 작은 거
            mid_box = carrots[i:j] # 중간
            large_box = carrots[j:] # 큰 거

            # 빈상자 있기만 해봐
            if len(small_box) == 0 or len(mid_box) == 0 or len(large_box) == 0:
                continue
            
            # 같은 크기면 같은 상자에 들어가자
            if small_box[-1] == mid_box[0] or mid_box[-1] == large_box[0]:
                continue
            
            # 자 이제 다 왔다 젤큰거 작은 거 차이는?
            max_size = max(len(small_box), len(mid_box), len(large_box))
            min_size = min(len(small_box), len(mid_box), len(large_box))

            carrots_diff = min(carrots_diff, max_size - min_size)
    # 포장못했힝구리퐁퐁
    if carrots_diff == 10000:
        return -1
    
    return carrots_diff

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    result = carrots_boxing(N, carrots)
    print(f'#{tc} {result}')