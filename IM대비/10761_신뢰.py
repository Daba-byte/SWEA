# def robot_trust(n, choice_list):
#     # 시간 변수 설정
#     time = 0
#     # 로봇들이 할 수 있는 행위는 3가지다. 움직이거나, 가만히 있거나, 버튼을 누르거나.
#     for i in choice_list:
#         if i == type(str):
#             # 오렌지 로봇의 선택
#             Orange_list = []
#             if i == O:
#                 Orange_list.append([i + 1])

#             # 블루 로봇의 선택
#             Blue_list = []
#             else:
#                 Blue_list.append([i + 1])
        
#         elif i == type(int):


#     return time

# T = int(input())
# for tc in range(1, T+1):
#     choice_list = list(map(input().split()))
#     n = choice_list[0]
#     choice_list = choice_list[1:]

#     result = robot_trust(n, choice_list)
#     print(f'#{tc} {result}')