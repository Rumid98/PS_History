import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    birth = input()
    n = int(input())
    codedays = [input() for _ in range(n)]
    max_bio = 0
    answer = ''
    for codeday in codedays:
        tmp = bio(birth, codeday)
        if tmp > max_bio:
            answer = codeday
            max_bio = tmp
        elif tmp == max_bio:
            answer = min(answer, codeday)
    print(answer)


def bio(a, b):
    y, m, d = 0, 0, 0
    for i in range(4):
        y += (int(a[i]) - int(b[i])) ** 2
    for i in range(4, 6):
        m += (int(a[i]) - int(b[i])) ** 2
    for i in range(6, 8):
        d += (int(a[i]) - int(b[i])) ** 2
    return y * m * d


if __name__ == "__main__":
    main()
