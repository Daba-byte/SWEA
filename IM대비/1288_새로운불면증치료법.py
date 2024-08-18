def count_sheep(N):
    # 이미 본 숫자들을 저장할 집합 (set)를 초기화
    seen_digits = set()
    # 배수를 계산하기 위한 변수 k를 초기화
    k = 0
    
    # 0부터 9까지의 모든 숫자를 보기 전까지 반복
    while len(seen_digits) < 10:
        # 배수를 증가시킴 (k = 1, 2, 3, ...)
        k += 1
        # 현재 배수에 대한 값을 계산 (예: k * N)
        current_number = k * N
        # 현재 배수의 숫자들을 set에 추가 (중복된 숫자는 자동으로 걸러짐)
        seen_digits.update(str(current_number))
    
    # 모든 숫자(0~9)를 보게 된 마지막 배수 (k * N)을 반환
    return k * N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = count_sheep(N)
    print(f"#{tc} {result}")