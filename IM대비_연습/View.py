def view(N, buildings):
    view_count = 0
    for i in range(2, N-2):
        max_height = max(buildings[i-1], buildings[i-2], buildings[i+1],buildings[i+2])
        if buildings[i] > max_height:
            view_count += buildings[i] - max_height                

    return view_count

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = view(N, buildings)
    print(f'#{tc} {result}')