def special_sort(N, ai):
    ai.sort()  # 오름차순 정렬
    
    new_ai = []
    
    # 큰 값과 작은 값을 번갈아가며 추가
    for i in range(N // 2):
        new_ai.append(ai[N - 1 - i])  # 큰 값 추가
        new_ai.append(ai[i])  # 작은 값 추가
    
    # N이 홀수인 경우 가운데 값을 마지막에 추가
    if N % 2 == 1:
        new_ai.append(ai[N // 2])
    
    # 10개까지만 출력
    return ' '.join(map(str, new_ai[:10]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    result = special_sort(N, ai)
    print(f'#{tc} {result}')