def find_real_number(binary, three_digit): # 정식이 짜증나
    binary_variants = [] # 이진수 후보들
    for i in range(len(binary)): # 이진수만큼 돌아
        if binary[i] == '1': # 1이면
            variant = binary[:i] + '0' + binary[i+1:] # 0으로 바꿔
        else: # 0이면
            variant = binary[:i] + '1' + binary[i+1:] # 1로 바꿔
        binary_variants.append(int(variant, 2)) # 10진수로 들어가

    third_digit_variants = [] # 3진수 후보들
    for i in range(len(three_digit)): # 3진수만큼 돌아
        for change in ['0', '1', '2']: # 바꿀 애들임
            if three_digit[i] != change: # 이거 아니면
                variant = three_digit[:i] + change + three_digit[i+1:] # 나머지 두개로 바꿔바
                third_digit_variants.append(int(variant, 3)) # 너도 10진수로 들어가삼

    for value in binary_variants: # 야 나 이진순데
        if value in third_digit_variants: # 삼진수 너 그 안에 나 있냐?
            return value # 어 나 찾았어?

T = int(input())
for tc in range(1, T+1):
    binary = input()
    three_digit = input()

    result = find_real_number(binary, three_digit)
    print(f'#{tc} {result}')

# 정식아 앞으로 그냥 10진수로 외우고 다니면 안되냐