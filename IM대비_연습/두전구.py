def two_lights(A, B, C, D):
    start = max(A, C)
    end = min(B, D)

    if start < end:
        return end - start
    else:
        return 0

T = int(input())
results = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    result = two_lights(A, B, C, D)
    results.append(f'#{tc} {result}')

for result in results:
    print(result)