import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    answer = [['.'] * (4*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = 'G'
            answer[n+i][n+j] = 'I'
            answer[2*n+i][2*n+j] = 'S'
            answer[n+i][3*n+j] = 'T'
    for i in range(3*n):
        for j in range(4*n):
            print(answer[i][j], end='')
        print()


if __name__ == "__main__":
    main()
