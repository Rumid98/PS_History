import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]


def bfs(x, y):
    answer = 0
    end = False
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    while queue and not end:
        le = len(queue)
        for i in range(le):
            tmp = queue.popleft()
            cx, cy = tmp[0], tmp[1]
            if cx == n - 1 and cy == m - 1:
                end = True
                break
            for j in range(4):
                nx, ny = cx + dx[j], cy + dy[j]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        answer += 1
    sys.stdout.write(str(answer))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*m for _ in range(n)]
bfs(0, 0)
