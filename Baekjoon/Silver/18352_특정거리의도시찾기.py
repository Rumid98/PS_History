import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
visited = [-1] * (n+1)  # 방문을 True/False 대신 출발지점부터의 거리로
city = [[] for _ in range(n+1)]
for _ in range(m):  # 단방향 도로 정보 입력
    a, b = map(int, input().split())
    city[a].append(b)


def bfs(v):  # 출발점부터 최단거리 k에 해당하는 모든 도시 출력 -> dfs가 아닌 bfs
    queue = deque()
    queue.append(v)
    visited[v] += 1  # 거리 증가
    while queue:
        cur = queue.popleft()
        for i in city[cur]:
            if visited[i] == -1:  # 처음 방문한 곳일 경우에만
                visited[i] = visited[cur] + 1  # 거리 1 증가
                queue.append(i)  # queue에 삽입


answer = []
bfs(x)
for i in range(n+1):
    if visited[i] == k:
        answer.append(i)
if not answer:
    sys.stdout.write('-1\n')
else:
    answer.sort()
    for j in answer:
        sys.stdout.write(str(j) + '\n')
