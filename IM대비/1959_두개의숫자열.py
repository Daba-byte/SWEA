def find_max(N, M, Ai, Bj):
    # Ai가 더 짧거나 같은 길이일 때
    if N <= M:
        max_sum = 0 # 최댓값을 저장할 변수
        for i in range(M - N + 1): # Bj를 Ai 길이만큼 슬라이딩
            current_sum = 0 # 곱셈 합을 저장할 변수
            for j in range(N): # Ai의 모든 원소와 대응하는 Bj의 원소 곱하기
                current_sum += Ai[j] * Bj[i + j]
            max_sum = max(max_sum, current_sum)
        return max_sum # 최댓값
    # Bj가 짧으면 Ai가 움직여서 곱해
    else: # 이 밑은 위랑 변수만 바뀌고 다 똑같아
        max_sum = 0
        for i in range(N - M + 1):
            current_sum = 0
            for j in range(M):
                current_sum += Ai[i + j] * Bj[j]
            max_sum = max(max_sum, current_sum)
        return  max_sum
 
T = int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    result = find_max(N, M, Ai, Bj)
    print(f'#{tc} {result}')