from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx, ny = tmp[0] + dx[i], tmp[1] + dy[i]
            # 끝부분 도달 처리
            if nx == n:
                nx = 0
            if nx == -1:
                nx = n - 1
            if ny == m:
                ny = 0
            if ny == -1:
                ny = m - 1
            # 방문하지 않은 0 위치인 경우 queue에 삽입, 방문 처리
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            answer += 1
print(answer)
