# 국기같은 인데 국기 같은으로 되어 있어서 나만 읽을 때 멈칫하는 거 아니잔아.
def like_russia_flag(N, M, flag): # 러시아 국기같은 깃발~
    # 비용 테이블 초기화 할거임
    white_cost = [0] * N # 얘네가
    blue_cost = [0] * N # 얼마나
    red_cost = [0] * N # 변경될 건지

    for i in range(N): # 색 바꿀 떄 필요한 비용은? 행 돌면서
        white_cost[i] = M - flag[i].count('W') # 해당 글자수가 아닌만큼
        blue_cost[i] = M - flag[i].count('B') # 글자를 세서
        red_cost[i] = M - flag[i].count('R') # 그 수 만큼 변경하는 비용으로 설정

    min_cost = 10000 # 최소 비용 계산 해야대

    # 난 왜이리 영역 나누기를 못할까 할 때마다 틀리네 개빡세
    for i in range(0, N-2): # 최소 행 2개응 남겨둬야 하니까
        for j in range(i+1, N-1): # 그다음 행부터, 마지막 행은 남겨야 하니까
            white_section = sum(white_cost[:i+1]) # 흰 구역 이만큼 써야한다
            blue_section = sum(blue_cost[i+1:j+1]) # 파랑은 이만큼
            red_section = sum(red_cost[j+1:]) # 빨강은 이만큼

            total_cost = white_section + blue_section + red_section # 총 비용은
            min_cost = min(min_cost, total_cost) # 근데 난 최소가 필요해

    return min_cost # 이만큼은 바꿔야 하걸랑

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    result = like_russia_flag(N, M, flag)
    print(f'#{tc} {result}')