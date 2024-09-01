def real_num(binary, three_digit):
    # 2진수에서 가능한 모든 한 자리 잘못된 경우
    binary_variants = [] # 경우의 숫자들 담을 리스트
    for i in range(len(binary)): # 이진수 돌면서
        if binary[i] == '0': # 문자열이 0이면
            variant = binary[:i] + '1' + binary[i+1:] # 1로 바꿔
        else: # 1이면
            variant = binary[:i] + '0' + binary[i+1:] # 0으로 바꿔
        binary_variants.append(int(variant, 2)) # 바꾼 2진수 10진수 숫자로 바꿔서 저장

    # 3진수에서 가능한 모든 한 자리 잘못된 경우
    three_digit_variants = [] # 경우의 숫자들22
    for i in range(len(three_digit)): # 3진수 돌면서
        for change in ['0', '1', '2']: # 얘네가
            if three_digit[i] != change: # 아니면
                variant = three_digit[:i] + change + three_digit[i+1:] # 바꿔봐
                three_digit_variants.append(int(variant, 3)) # 다 숫자로 들어가

    # 2진수 경우와 3진수 경우 중 같은 값 찾기
    for value in binary_variants: # 2진수에도 있고
        if value in three_digit_variants: # 3진수에도 있는 넌 누구야
            return value # 나야

T = int(input())
for tc in range(1, T+1):
    binary = input().strip()
    three_digit = input().strip()

    result = real_num(binary, three_digit)
    print(f'#{tc} {result}')