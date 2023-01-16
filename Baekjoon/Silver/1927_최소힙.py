import sys
import heapq
input = sys.stdin.readline
n = int(input())
queue = []


for i in range(n):
    command = int(input())
    if command == 0:
        if not queue:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write(str(heapq.heappop(queue)) + '\n')
    else:
        heapq.heappush(queue, command)
