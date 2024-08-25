def bbiribbaribbo(numbers):
    # 어라 나외계인인가 외계어가 읽히는데
    number_dict = {"ZRO" : 0 , "ONE": 0 , "TWO": 0 , "THR": 0 , "FOR": 0 ,
                   "FIV": 0 , "SIX": 0 , "SVN": 0 , "EGT": 0 , "NIN": 0 }

    for i in numbers: # 입력 받은 외계어 돌면서
        if i in number_dict: # 외계어가 딕셔너리에 있으면
            number_dict[i] += 1 # 벨류 올려

    sorted_numbers = [] # 정리할 리스트 만들고
    # 외계어 리스트 돌면서
    for key in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]:
        # 정리 리스트에 순서대로 넣어버려 키 개수만큼
        # extend가 뭐에요? 반복 가능한 객체에서 요소들을 추가하는 메서드
        sorted_numbers.extend([key] * number_dict[key])

    return ' '.join(sorted_numbers)

T = int(input())
for test_case in range(1, T + 1):
    number = list(input().split())
    num = int(number[1])
    numbers = list(input().split())
    
    result = bbiribbaribbo(numbers)
    print(f'#{test_case} {result}')