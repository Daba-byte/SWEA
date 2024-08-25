def move_box(N, arr):
    for _ in range(N): # N번 덤프 실행
        # 가장 높은 곳과 낮은 곳 찾기
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))

        # 평탄화 완료시 멈춤
        if arr[max_idx] - arr[min_idx] <= 1:
            break
        
        # 가장 높은 곳에서 낮은 곳으로 옮김
        arr[max_idx] -= 1
        arr[min_idx] += 1

    return max(arr) - min(arr)

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = move_box(N, arr)
    print(f'#{tc} {result}')