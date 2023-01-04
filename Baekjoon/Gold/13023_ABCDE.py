import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0


# A, B, C, D, E 총 5개의 연속된 친구관계가 존재하면 1, 그렇지 않으면 0을 출력하는 문제
def dfs(a, count):
    global answer
    if count == 5:
        answer = 1
        return
    visited[a] = True
    for x in graph[a]:
        if not visited[x]:
            dfs(x, count + 1)
    visited[a] = False


# n의 최대가 2,000이므로, 전체를 탐색해도 괜찮다
visited = [False] * (n + 1)
for i in range(n):
    dfs(i, 1)
    if answer == 1:
        break
sys.stdout.write(str(answer))
