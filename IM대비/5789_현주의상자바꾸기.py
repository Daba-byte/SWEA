# 언니 박스 왜 바꿔 걍 써주면 안될까
# 그래도 내가 언니니까 바꿔주는 거야
def hyunju_do_not_change_box(N, Q, operations):
    box = [0] * N
    for i in range(1, Q + 1):
        L, R = operations[i - 1]
        for j in range(L - 1, R):
            box[j] = i
    return box

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    operations = []
    for _ in range(Q):
        L, R = map(int, input().split())
        operations.append((L, R))
    
    result = hyunju_do_not_change_box(N, Q, operations)
    print(f'#{tc} ', *result)

######  좀 더 간단 #####

T = int(input())

for t in range(1, T + 1):
    # 각 테스트 케이스에 대한 입력
    N, Q = map(int, input().split())
    boxes = [0] * N
    
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        # 상자 값 업데이트
        for j in range(L - 1, R):
            boxes[j] = i
            
    # 결과 출력
    print(f"#{t}", *boxes)
