def carrots(N, C_list):
    max_carrots = 0
    carrots_index = 0

    for i in range(N):
        if C_list[i] > max_carrots:
            max_carrots = C_list[i] # 당근 젤 마나
            carrots_index = i + 1 # 인덱스 저장
        elif C_list[i] == max_carrots:
            continue # 이미 가장 큰 값 저장했으니까 무시

    return f'{carrots_index} {max_carrots}'

T =  int(input())
for tc in range(1, T+1):
    N = int(input())
    C_list = list(map(int, input().split()))

    result = carrots(N, C_list)
    print(f'#{tc} {result}')