import sys
import heapq
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    tmp = list(map(int, input().split()))
    queue = []
    for x in tmp:
        heapq.heappush(queue, x)
    answer = 0
    while len(queue) != 1:
        a, b = heapq.heappop(queue), heapq.heappop(queue)
        answer += (a*b)
        heapq.heappush(queue, a+b)
    print(answer)


if __name__ == "__main__":
    main()