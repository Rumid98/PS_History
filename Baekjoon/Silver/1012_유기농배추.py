import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# bfs 함수 선언
def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:  # 인접한 곳에 배추가 있을 경우
        cur = queue.popleft()
        for k in range(4):  # 상하좌우 탐색
            nx, ny = cur[0] + dx[k], cur[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = 0
    for _ in range(k):  # k개 만큼 1 대입
        y, x = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                answer += 1
    sys.stdout.write(str(answer) + '\n')
