import sys
import heapq
input = sys.stdin.readline


X = int(input())
queue = []
heapq.heappush(queue, 64)

while True:
    if sum(queue) == X:
        break
    min_value = heapq.heappop(queue)
    if sum(queue) + min_value//2 >= X:
        heapq.heappush(queue, min_value//2)
    else:
        for _ in range(2):
            heapq.heappush(queue, min_value//2)
        
print(len(queue))
