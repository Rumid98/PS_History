import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

s = int(input())
tmp = list(map(int, input().split()))
gomgom = [False] * (n+1)
for x in tmp:
    gomgom[x] = True

def DFS(v):
    global answer
    if gomgom[v]:
        return
    if not graph[v]:
        answer = -1
        return
    for next_node in graph[v]:
        DFS(next_node)

DFS(1)
print('Yes') if answer == 1 else print('yes')