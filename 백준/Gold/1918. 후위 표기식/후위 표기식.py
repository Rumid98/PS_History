import sys
def input(): return sys.stdin.readline().strip()


def main():
    infix = list(input())
    priority = {'+': 3, '-': 3, '*': 2, '/': 2, '(': 1}
    operator = []
    answer = ''
    for c in infix:
        if c.isalpha():
            answer += c
        else:
            if c == '+' or c == '-' or c == '*' or c == '/':
                if not operator:
                    operator.append(c)
                else:
                    while operator:
                        if priority[c] >= priority[operator[-1]] and operator[-1] != '(':
                            answer += operator.pop()
                        else:
                            break
                    operator.append(c)
            elif c == '(':
                operator.append(c)
            elif c == ')':
                while operator[-1] != '(':
                    answer += operator.pop()
                operator.pop()
    while operator:
        answer += operator.pop()
    print(answer)


if __name__ == "__main__":
    main()
