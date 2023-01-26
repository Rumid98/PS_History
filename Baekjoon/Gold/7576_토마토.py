import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())  # 토마토 상자의 가로, 세로
graph = [list(map(int, input().split())) for _ in range(n)]  # 토마토가 들어있는 상자 입력
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():  # 탐색 함수 정의
    count = 0  # 영향을 줄 수 있는 범위가 모두 익을 때까지의 최소 날짜
    while queue:
        changed = False  # 변경이 되었을 때만 날짜 +1 해주기 위함
        date_len = len(queue)  # 한 날짜에 탐색해야하는 영역 개수
        for _ in range(date_len):  # 해당 개수만큼 탐색 시작
            cur = queue.popleft()
            for i in range(4):  # 상하좌우 탐색
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]
                if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and not visited[nx][ny]:
                    graph[nx][ny] = 1  # 접촉 후 익었으므로 1로 변경
                    changed = True  # 변경 check
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny))  # queue에 탐색 영역 삽입
        if changed:
            count += 1  # 해당 개수만큼 탐색 완료 시 +1 (날짜 +1)
    return count


# 상자를 한 번 전체 탐색 후 토마토가 들어있는 위치를 queue에 전부 넣어준 후에 bfs 진행
queue = deque()
visited = [[False] * (m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))  # queue에 위치값 삽입
            visited[i][j] = True
answer = bfs()
checked = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            checked = False
if checked:
    sys.stdout.write(str(answer))
else:
    sys.stdout.write('-1\n')
