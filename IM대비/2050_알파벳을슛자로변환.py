# 문자열 입력
input_string = input().strip()

# 결과를 저장할 리스트
result = []

# 문자열의 각 알파벳을 숫자로 변환
for char in input_string:
    # 'A'의 아스키 코드는 65, 'a'의 아스키 코드는 97이므로
    # ord(char) - ord('A') + 1 또는 ord(char) - 64로 변환 가능
    number = ord(char.upper()) - ord('A') + 1
    result.append(str(number))

# 변환된 숫자들을 공백으로 구분하여 출력
print(" ".join(result))