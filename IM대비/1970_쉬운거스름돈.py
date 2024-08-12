def dondon(N):
    # 화폐 단위를 큰 금액부터 작은 금액 순으로 나열
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    won_list = []
 
    for unit in units:
        won_list.append(N // unit)  # 해당 단위의 개수를 리스트에 추가
        N %= unit  # 잔액 업데이트
 
    return won_list
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = dondon(N)
    print(f'#{tc}')
    print(' '.join(map(str, result)))

###################################
# 재귀 사용
# def dondon(N, won_list=None):
#     if won_list is None:
#         won_list = [0] * 8  # 각 화폐 단위별 개수를 저장할 리스트 초기화
 
#     # 화폐 단위와 인덱스 매핑
#     units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
 
#     if N == 0:
#         return won_list
 
#     for i, unit in enumerate(units):
#         if N >= unit:
#             won_list[i] += N // unit
#             N = N % unit
#             return dondon(N, won_list)
 
#     return won_list
 
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     result = dondon(N)
#     print(f'#{tc}')
#     print(' '.join(map(str, result)))