from collections import deque
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [0, 0, 0, 0, 1, -1]  # x축 이동
dy = [0, 0, 1, -1, 0, 0]  # y축 이동
dz = [1, -1, 0, 0, 0, 0]  # z축 이동
queue = deque()  # 덱 배열
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]  # 방문 체크 배열
answer = 0

def bfs():
    count = 0
    while queue:
        changed = False
        q_len = len(queue)  # 하루동안 체크해야하는 토마토 개수
        for _ in range(q_len):
            x, y, z = queue.popleft()  # 체크할 좌표
            for i in range(6):  # 6방향 탐색
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:  # 상자 범위 안에 존재하는지 판단
                    if graph[nz][nx][ny] == 0 and not visited[nz][nx][ny]:  # 좌표가 0이고, 방문하지 않은 경우
                        changed = True
                        visited[nz][nx][ny] = True  # 방문 처리
                        graph[nz][nx][ny] = 1  # 익음(1) 처리
                        queue.append((nx, ny, nz))  # 해당 좌표 queue에 삽입
        if changed:
            count += 1
            changed = False
    return count


# 토마토가 있는 칸 탐색
for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 1:
                visited[k][i][j] = True
                queue.append((i, j, k))
answer = bfs()  # bfs 전개
# 남은 칸이 있는지 탐색
clear = True
for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 0:
                clear = False
if clear:
    print(answer)
else:
    print('-1')
