import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
g_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g_list[u].append(v)
    g_list[v].append(u)
visited = [False] * (n + 1)
answer = 0


def dfs(a):
    visited[a] = True
    for x in g_list[a]:
        if not visited[x]:
            dfs(x)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1
sys.stdout.write(str(answer))
