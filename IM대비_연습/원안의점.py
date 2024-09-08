def dot_in_circle(N):
    dot_count = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if i ** 2 + j ** 2 <= N ** 2:
                dot_count += 1

    return dot_count

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = dot_in_circle(N)
    print(f'#{tc} {result}')