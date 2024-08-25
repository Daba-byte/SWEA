def sort_number(N, N_list):
    for i in range(N - 1): # 마지막은 이미 정렬된 상태라서 정렬할 필요 없음
        min_idx = i # 일단 i가 가장 작다 치자
        for j in range(i+1, N): # i 빼고 봐바
            if N_list[min_idx] > N_list[j]: # 엥 근데 작다 친 거 보다 다른 게 더 작네?
                min_idx = j # 그럼 네가 젤 작아
        # 정리 깔쌈하게 해라        
        N_list[i], N_list[min_idx] = N_list[min_idx], N_list[i]
    
    return N_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    sorted_list = sort_number(N, N_list)
    result = " ".join(map(str, sorted_list))
    print(f'#{tc} {result}')