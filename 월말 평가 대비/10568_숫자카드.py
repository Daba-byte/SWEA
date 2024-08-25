def card_game(N, numbers):
    arr =[0] * 10
    max_num = -1
    max_card = -1

    # 숫자 빈도수 카운트
    for num in numbers:
        arr[num] += 1

    # 가장 많은 숫자 찾기
    for i in range(10):
        if arr[i] > max_num:
            max_num = arr[i]
            max_card = i
        elif arr[i] == max_num and i > max_card:
            max_card = i

    return max_card, max_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().strip()))

    max_card, max_num = card_game(N, numbers)
    print(f'#{tc} {max_card} {max_num}')