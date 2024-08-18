T = 10  # 테스트 케이스는 항상 10개
for tc in range(1, T + 1):
    size = int(input())  # 테이블의 크기 (항상 100)
    table = [list(map(int, input().split())) for _ in range(size)]
    
    count = 0  # 교착 상태의 개수
    
    for col in range(size):
        prev = 0
        for row in range(size):
            if table[row][col] == 1:  # N극 성질의 자성체
                prev = 1
            elif table[row][col] == 2:  # S극 성질의 자성체
                if prev == 1:  # 이전 자성체가 N극 성질일 경우 교착 상태 발생
                    count += 1
                prev = 0
    
    print(f"#{tc} {count}")