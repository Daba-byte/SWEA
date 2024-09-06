def find_max_card(N, cards):
    card = {} # 자주 나올 카드 빈도를 확인할 딕셔너리

    for i in range(N): # N번 돌면서
        if cards[i] in card: # 카드 더미에 카드가 딕셔너리에 있다면
            card[cards[i]] += 1 # 갯수 올려
        else: # 없다면
            card[cards[i]] = 1 # 딕셔너리에 추가

    max_num, many_num = -1, -1 # 갯수와 카드 번호 확인할 변수 초기화

    # 가장 많은 숫자 카드와 카드 번호 확인
    for num, count in card.items():
        if count > many_num:
            many_num = count
        if count == many_num and num > max_num:
            max_num = num

    return max_num, many_num


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().strip()))

    result = find_max_card(N, cards)
    x, y = result
    print(f'#{tc} {x} {y}')