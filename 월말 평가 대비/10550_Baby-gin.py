def baby_gin(numbers):
    count = [0] * 10

    for num in numbers:
        count[num] += 1

    triplet = 0
    runs = 0

    i= 0
    while i < 10:
        if count[i] >= 3:
            count[i] -= 3
            triplet += 1
            continue

        if i <= 7 and count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            runs += 1
            continue

        i += 1

    if triplet + runs == 2:
        return 'Baby gin'
    else:
        return 'Lose'

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().strip()))

    result = baby_gin(numbers)
    print(f'#{tc} {result}')