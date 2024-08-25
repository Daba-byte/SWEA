def binary_search(P, target):
    l = 1
    r = P
    count = 0

    while l <= r:
        center = int((l+r)//2)
        count += 1

        if center == target:
            return count
        elif center < target:
            l = center
        else:
            r = center

    return count

def pigonhae(P, Pa, Pb):
    A_count = binary_search(P, Pa)
    B_count = binary_search(P, Pb)

    if A_count < B_count:
        return 'A'
    elif B_count < A_count:
        return 'B'
    else:
        return '0'

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    result = pigonhae(P, Pa, Pb)
    print(f'#{tc} {result}')

#### 주노 강사님이 알려주신 코드 ###
T = int(input())

def binary_search(start, end, key, cnt):
    mid = (start + end) // 2
    if key == mid:
        return cnt
    elif key < mid:
        cnt += 1
        return binary_search(start, mid, key, cnt)
    elif key > mid:
        cnt += 1
        return binary_search(mid, end, key, cnt)


for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    A_cnt = binary_search(1, P, A, 1)
    B_cnt = binary_search(1, P, B, 1)
    if A_cnt == B_cnt:
        print(f"#{test_case} 0")
    elif A_cnt < B_cnt:
        print(f"#{test_case} A")
    elif A_cnt > B_cnt:
        print(f"#{test_case} B")