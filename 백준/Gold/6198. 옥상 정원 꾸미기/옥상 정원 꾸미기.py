import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    buildings = [int(input()) for _ in range(n)]
    answer = [0] * n
    stack = [(0, buildings[0])]
    for i in range(1, n):
        if buildings[i] < stack[-1][1]:
            stack.append((i, buildings[i]))
        else:
            while stack:
                if buildings[i] >= stack[-1][1]:
                    b = stack.pop()
                    answer[b[0]] = i-b[0]-1
                else:
                    break
            stack.append((i, buildings[i]))
    while stack:
        if 1_000_000_001 >= stack[-1][1]:
            b = stack.pop()
            answer[b[0]] = n-b[0]-1
        else:
            break
    print(sum(answer))


if __name__ == "__main__":
    main()
