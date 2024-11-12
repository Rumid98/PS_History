import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                answer[v] += 1
                visited[next_node] = True

for i in range(1, n+1):
    visited = [False] * (n+1)
    BFS(i)
max_value = max(answer)
for i in range(1, n+1):
    if answer[i] == max_value:
        print(i, end=' ')
