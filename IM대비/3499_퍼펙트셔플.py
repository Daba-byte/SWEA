T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()

    mid = (N + 1) // 2
    cards1 = cards[:mid]
    cards2 = cards[mid:]

    new_cards = []
    for i in range(len(cards2)):
        new_cards.append(cards1[i])
        new_cards.append(cards2[i])
    
    # cards1이 더 길 경우 남은 요소 추가
    if len(cards1) > len(cards2):
        new_cards.append(cards1[-1])

    print(f'#{tc} {" ".join(new_cards)}')

##### 힘들어 더 못하겠어 #####

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()
    
    # 덱을 절반으로 나누기
    mid = (N + 1) // 2  # N이 홀수일 때 앞쪽 덱이 하나 더 많도록
    first_half = cards[:mid]
    second_half = cards[mid:]
    
    shuffled_deck = []
    # 두 덱에서 교대로 카드를 뽑아 새로운 덱을 만듦
    for i in range(mid):
        shuffled_deck.append(first_half[i])
        if i < len(second_half):
            shuffled_deck.append(second_half[i])
    
    print(f"#{tc} {' '.join(shuffled_deck)}")