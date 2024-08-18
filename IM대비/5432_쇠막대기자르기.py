def count_cut_pieces(expression):
    stack = []
    total_pieces = 0
    i = 0
    
    while i < len(expression):
        if expression[i] == '(':
            stack.append('(')
        else:
            # 닫는 괄호를 만났을 때
            if expression[i - 1] == '(':
                # 레이저인 경우
                stack.pop()
                total_pieces += len(stack)
            else:
                # 쇠막대기의 끝인 경우
                stack.pop()
                total_pieces += 1
        i += 1

    return total_pieces

T = int(input())
for t in range(1, T + 1):
    expression = input().strip()
    result = count_cut_pieces(expression)
    print(f"#{t} {result}")