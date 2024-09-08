def turn_switch(N, before, after): # ptsd 오자낭..
    switch_count = 0 # 이겨낸다
    for i in range(N):
        if before[i] != after[i]: # 안똑같으면
            switch_count += 1 # 일단 바꾸니까 카운트 올려
            for j in range(i, N):
                before[j] = 1- before[j] # ㄹㅇ 바꿔

    return switch_count # ㅋㅋ 아이엠 딱대 개쉽네

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    result = turn_switch(N, before, after)
    print(f'#{tc} {result}')