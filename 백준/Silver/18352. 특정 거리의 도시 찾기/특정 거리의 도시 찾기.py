import sys
from collections import deque
input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[x] = True
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
queue = deque()
queue.append(x)
count = 0
while queue:
    if count == k:
        for node in sorted(list(queue)):
            print(node)
        break
    cur_len = len(queue)
    for _ in range(cur_len):
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    count += 1
else:
    print(-1)
