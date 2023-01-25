import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        cur = queue.popleft()
        for x in graph[cur]:
            if not visited[x]:
                queue.append(x)
                check[x] += 1  # 신뢰도에 따라 갈 수 있으면 횟수 +1
                visited[x] = True


check = [0] * (n+1)
for i in range(1, n+1):
    visited = [False] * (n + 1)
    bfs(i)
max_value = max(check)
for i in range(n+1):
    if check[i] == max_value:
        sys.stdout.write(str(i) + ' ')
