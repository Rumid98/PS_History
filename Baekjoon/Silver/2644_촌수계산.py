from collections import deque

n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
queue = deque()
queue.append(x)
count = 0
while queue:
    cur_len = len(queue)
    found = False
    for _ in range(cur_len):
        cur_node = queue.popleft()
        if cur_node == y:
            found = True
            break
        if graph[cur_node]:
            for node in graph[cur_node]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
    if found:
        break
    count += 1
else:
    count = -1
print(count)
