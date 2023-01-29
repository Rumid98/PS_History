import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 1
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# n의 최대는 100, n^2는 10,000 -> 브루트포스로 해결 가능
def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


def rain():  # 배열 각 요소별로 1씩 뺴주는 함수
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                graph[i][j] -= 1


highest = 0  # 탐색 범위 지정
for i in range(n):
    for j in range(n):
        if graph[i][j] > highest:
            highest = graph[i][j]
for i in range(1, highest):
    visited = [[False] * n for _ in range(n)]
    rain()
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > 0 and not visited[j][k]:
                bfs(j, k)
                count += 1
    answer = max(answer, count)
sys.stdout.write(str(answer))
