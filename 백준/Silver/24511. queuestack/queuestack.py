import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    queue = deque()
    qs = list(map(int, input().split()))
    qs_number = list(map(int, input().split()))
    for i in range(n):
        if qs[i] == 0:
            queue.append(qs_number[i])
    m = int(input())
    input_number = list(map(int, input().split()))
    for x in input_number:
        queue.appendleft(x)
        print(queue.pop(), end=' ')


if __name__ == "__main__":
    main()
