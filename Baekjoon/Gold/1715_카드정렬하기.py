import sys
import heapq
input = sys.stdin.readline
n = int(input())
queue = []  # 힙 사욜할 list 선언
for i in range(n):
    heapq.heappush(queue, int(input()))


# 작은 수부터 합 진행해야 최소가 된다
answer = 0
while len(queue) != 1:  # 한 개만 남을 때까지 진행
    a, b = heapq.heappop(queue), heapq.heappop(queue)
    answer += (a + b)
    heapq.heappush(queue, a+b)
sys.stdout.write(str(answer))
