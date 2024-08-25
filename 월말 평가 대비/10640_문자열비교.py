def geajolryea(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = geajolryea(str1, str2)
    print(f'#{tc} {result}')

### for문 쓰자 ###
def geajolryea(str1, str2):
    for i in range(len(str2) - len(str1) +1):
        if str2[i:i + len(str1)] == str1:
            return 1
    return 0 # 반복문 끝나도 없으면 0 반환 else 금지

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = geajolryea(str1, str2)
    print(f'#{tc} {result}')