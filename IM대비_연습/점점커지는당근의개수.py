def increase_carrots(N, carrots): # 당근 증가 길이
    carrots_count, crr_cnt = 1, 1 # 기본 값 세팅
    for i in range(N - 1): # 마지막은 비교할 거가 없으니께
        if carrots[i] < carrots[i + 1]: # 다음 당근이 내 당근보다 크면
            crr_cnt += 1 # 카운트 올려
            carrots_count = max(carrots_count, crr_cnt) # 젤 큰 카운트 내놔

        else: # 작거나 같으면
            crr_cnt = 1 # 다시 1부터

    return carrots_count # 최대 길이는?


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    result = increase_carrots(N, carrots)
    print(f'#{tc} {result}')