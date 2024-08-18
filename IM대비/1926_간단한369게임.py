N = int(input())
game = []
for i in range(1, N+1):
    str_i = str(i) # 문자열로 변경
    clap = 0 # 박수 횟수
    for char in str_i:
        if char in '369': # 만약 369가 있다면
            clap += 1 #박수
    # 박수 쳐야할 때
    if clap > 0:
        game.append('-' * clap)
    # 아니면 걍 넣어
    else:
        game.append(i)

print(*game)