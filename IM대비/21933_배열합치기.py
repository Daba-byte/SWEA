def merong(N, M, A, B):
    C = []
    i, j = 0, 0

    # 교대로 배열 A, B 요소를 C에 추가
    while i < N and j < M:
        C.append(A[i])
        C.append(B[j])
        i += 1
        j += 1

    # 배열 A 남은 요소 추가
    while i < N:
        C.append(A[i])
        i += 1
    # 배열 B 남은 요소 추가
    while j < M:
        C.append(B[j])
        j += 1

    return C

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = merong(N, M, A, B)
    print(f'#{tc}', *result)

###### for문으로 풀어보자 #######
def merong(N, M, A, B):
    C = []
    
    # 최소 길이를 기준으로 교대로 요소 추가
    min_length = min(N, M)
    for i in range(min_length):
        C.append(A[i])
        C.append(B[i])
    
    # 배열 A의 남은 요소 추가
    for i in range(min_length, N):
        C.append(A[i])
    
    # 배열 B의 남은 요소 추가
    for i in range(min_length, M):
        C.append(B[i])

    return C

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = merong(N, M, A, B)
    print(f'#{tc}', *result)