def light(A, B, C, D):

    start = max(A, C) # 두 전구 시작점 중 큰 거
    end = min(B, D) # 두 전구 끝점 중 작은 거

    if start < end: # 만약 시작점이 작으면
        return end - start # 이만큼 같이 켜짐
    else: # 아니면
        return 0 # 안 겹침


T = int(input())

results = []  # 결과를 저장할 리스트

for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    result = light(A, B, C, D) 
    results.append(f"#{tc} {result}")  # 테스트 케이스 번호와 결과 저장

# 모든 결과 한 번에 출력
for result in results:
    print(result)

#########
# 미친 문제 뭔 출력을 이렇게하게 만들어서
# 킹치만 덕분에 웃었다