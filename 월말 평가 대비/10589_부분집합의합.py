# 부분집합 연산시 비트 연산자'<<' 사용하기
def himdureoyo(N, K):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ans = 0

    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])

        if len(subset) == N and sum(subset) == K:
            ans += 1

    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    result = himdureoyo(N, K)
    print(f'#{tc} {result}')