def bunguh(N, M, K, people):
    people.sort()  # 손님 도착 시간을 오름차순으로 정렬
    for i in range(N):
        time = people[i]
        bbang = (time // M) * K  # 현재 시점까지 만들어진 붕어빵의 수
        if bbang < i + 1:  # 필요한 붕어빵의 수보다 적다면
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    result = bunguh(N, M, K, people)
    print(f'#{tc} {result}')