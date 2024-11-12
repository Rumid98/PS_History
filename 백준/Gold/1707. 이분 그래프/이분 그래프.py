import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
answer = True
    
def DFS(v):
    global answer    
    for nv in graph[v]:
        if visited[nv]:
            if node_value[v] == node_value[nv]:
                answer = False
                return
        else:
            visited[nv] = True
            if node_value[v] == 1:
                node_value[nv] = 2
            else:
                node_value[nv] = 1
            DFS(nv)

t = int(input())
for _ in range(t):
    answer = True
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v+1)
    node_value = [0] * (v+1)
    for i in range(1, v+1):
        if not visited[i]:
            visited[i] = True
            node_value[i] = 1
            DFS(i)
    print('YES') if answer else print('NO')
