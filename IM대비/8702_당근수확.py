def banibani_danggun_danggun(N, carrot_list):
    total_carrots = sum(carrot_list) # 전체 당근의 합
 
    # 첫 번째 일꾼이 수확한 당근 수와 두 번째 일꾼이 수확한 당근 수의 차이의 최소값
    min_diff = 100
    partition_index = 0
 
    # 첫 번째 일꾼의 누적 당근 수
    first_worker_sum = 0
 
    # i번째 구역까지 첫 번째 일꾼이 수확할 때
    for i in range(1, N):
        first_worker_sum += carrot_list[i - 1]
        second_worker_sum = total_carrots - first_worker_sum
        diff = abs(first_worker_sum - second_worker_sum)
         
        if diff < min_diff:
            min_diff = diff
            partition_index = i
 
    return f'{partition_index} {min_diff}'
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
     
    danggun = banibani_danggun_danggun(N, carrot_list)
    print(f'#{tc} {danggun}')