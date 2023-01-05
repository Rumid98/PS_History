import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# dfs 함수 선언
def dfs(a):
    sys.stdout.write(str(a) + ' ')
    visited[a] = True
    for j in graph[a]:
        if not visited[j]:
            dfs(j)


# bfs 함수 선언
def bfs(b):
    queue = deque()
    queue.append(b)
    visited[b] = True
    while queue:
        tmp = queue.popleft()
        sys.stdout.write(str(tmp) + ' ')
        for k in graph[tmp]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)


# 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문 -> 정렬 필요
for i in range(1, n + 1):
    graph[i].sort()
visited = [False] * (n + 1)
dfs(v)
sys.stdout.write('\n')
visited = [False] * (n + 1)
bfs(v)
