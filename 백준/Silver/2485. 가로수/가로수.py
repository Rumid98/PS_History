import sys
import heapq
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    heap = []
    total_min, total_max = 0, 0
    for _ in range(n):
        heap.append(int(input()))
    heapq.heapify(heap)
    a = heapq.heappop(heap)
    GCD = heap[0] - a
    total_min = a

    while len(heap) > 1:
        tmp = heapq.heappop(heap)
        GCD = gcd(GCD, heap[0]-tmp)
    total_max = heap[0]

    total_length = total_max - total_min
    total_count = total_length // GCD - n + 1
    print(total_count)


def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x


if __name__ == "__main__":
    main()
