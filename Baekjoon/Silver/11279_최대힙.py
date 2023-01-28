import sys
import heapq
input = sys.stdin.readline
n = int(input())


# 자연수만 입력받으므로, 마이너스(-)화 해서 힙에 삽입 -> 가장 큰 수가 가장 작아지게 됨
queue = []
for i in range(n):
    command = int(input())
    if command == 0:
        if queue:
            sys.stdout.write(str(abs(heapq.heappop(queue))) + '\n')
        else:
            sys.stdout.write('0\n')
    else:
        heapq.heappush(queue, command*(-1))
