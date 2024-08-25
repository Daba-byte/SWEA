def find_len(str1, str2):
    max_count = 0
    
    char_count = {}
    for char in str2: # 긴 문자열 돌면서
        if char in char_count: # 문자가 딕셔너리에 있으면
            char_count[char] += 1 # 딕셔너리 벨류 올려
        else: # 없으면
            char_count[char] = 1 # 딕셔너리에 추가해

    for char in str1: # 자이제 작은 문자열 돌명서
        if char in char_count: #문자가 딕셔너리에 있고
            if char_count[char] > max_count: # 딕셔너리 벨류가 맥스보다 크면
                max_count = char_count[char] # 실은 너가 젤 많은 값이다 이 말이야

    return max_count

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = find_len(str1, str2)
    print(f'#{tc} {result}')