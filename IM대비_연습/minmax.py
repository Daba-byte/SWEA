def min_max(ai):
    max_num = - 10000000000
    min_num = 1000000000
    for i in ai:
        if max_num < i:
            max_num = i
        elif min_num > i:
            min_num = i

    return max_num - min_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    result = min_max(ai)
    print(f'#{tc} {result}')