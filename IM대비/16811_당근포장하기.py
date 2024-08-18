def carrot(N, carrots):
    carrots.sort()
    ans = 10000
    # i, j는 각 상자에 들어갈 당근 개수를 정하는 기준점
    for i in range(N-2):
        for j in range(i+1, N-1):
            box1 = carrots[:i+1]        # 0 -> i 당근 포장
            box2 = carrots[i+1:j+1]     # i+1 -> j 당근 포장
            box3 = carrots[j+1:]        # j+1 -> N-1 당근 포장
            if box1[-1] != box2[0] and box2[-1]!= box3[0]: # 같은 크기 당근이 다른 상자에 들어가는 경우 방지
                n1, n2, n3 = len(box1), len(box2), len(box3)        # 각 상자의 당근 개수
                if max(n1, n2, n3) <= N//2: # 모든 상자가 N//2개 이내
                    if ans > max(n1, n2, n3) - min(n1, n2, n3):     # 당근 수의 차이가 최소인 경우
                        ans = max(n1, n2, n3) - min(n1, n2, n3)     
    if ans == 10000:
        ans = -1
    return ans

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    result = carrot(N, carrots)
    print(f'#{tc} {result}')