from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
queue = deque()
answer = []
for i in range(1, N+1):
    queue.append(i)
    
while len(queue) > 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())

for i in range(N-1):
    print(answer[i], end=' ')
print(queue[0])