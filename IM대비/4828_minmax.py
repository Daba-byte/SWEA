def min_max(N, ai):
    min_number = 100000000
    max_number = 0
     
    for num in ai:
        if min_number > num:
            min_number = num
        if max_number < num:
            max_number = num
             
    return max_number - min_number
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = min_max(N, ai)
    print(f'#{tc} {result}')