from collections import deque


def bfs():
    queue = deque()
    visited[1] = True
    queue.append(1)
    while queue:
        cur_node = queue.popleft()
        for x in nodes[cur_node]:
            if not visited[x]:
                answer[x] = str(cur_node)
                visited[x] = True
                queue.append(x)


n = int(input())
nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = ['' for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
bfs()
print('\n'.join(answer[2:]))
