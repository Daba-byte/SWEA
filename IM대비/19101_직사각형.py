def classify_rectangle_overlap(x1, y1, p1, q1, x2, y2, p2, q2):
    # 두 직사각형이 완전히 분리된 경우
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        return 4
    
    # 겹치는 부분이 점인 경우
    if (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2):
        return 3
    
    # 겹치는 부분이 선분인 경우
    if p1 == x2 or p2 == x1:
        if (y1 <= q2 and q1 >= y2):
            return 2
    if q1 == y2 or q2 == y1:
        if (x1 <= p2 and p1 >= x2):
            return 2
    
    # 겹치는 부분이 직사각형인 경우
    return 1

T = int(input())
for tc in range(1, T+1):
    x1, y1, p1, q1 = map(int, input().split()) # 첫번째 사각형 정보
    x2, y2, p2, q2 = map(int, input().split()) # 두번쨰 사각형 정보
    result = classify_rectangle_overlap(x1, y1, p1, q1, x2, y2, p2, q2)
    print(f'#{tc} {result}')