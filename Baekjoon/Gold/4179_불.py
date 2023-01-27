import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())  # 행, 열 개수 입력
graph = [list(input()) for _ in range(r)]  # 미로 정보 입력
answer = 0  # 탈출 시간 계산
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 지훈이는 빈공간에 한해서 이동, 불은 벽을 제외한 나머지 공간 이동 가능 / 지훈, 불 각각 방문 설정
# queue 탐색 도중 지훈이가 사라지면 탐색 종료 / 지훈이가 미로의 가장자리에 다다르면 종료(성공)
def bfs():  # 탐색 함수 선언
    global answer
    while queue:
        answer += 1
        if queue[0][1] != 'J':  # 지훈이가 더이상 존재하지 않는다면 종료
            return False
        queue_len = len(queue)
        for _ in range(queue_len):  # 현재 queue 길이만큼 loop 진행
            cur = queue.popleft()
            if cur[1] == 'J':  # 현재 node가 지훈이인 경우
                if f_visited[cur[0][0]][cur[0][1]]:  # 이미 불이 번진 경우 제외
                    continue
                if (cur[0][0] == 0 or cur[0][0] == (r - 1) or cur[0][1] == 0 or cur[0][1] == (c - 1)):  # 지훈이의 위치가 이미 탈출 가능한 경우
                    return True
                for d in range(4):  # 상하좌우 탐색
                    nx, ny = cur[0][0] + dx[d], cur[0][1] + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and not j_visited[nx][ny]:  # 미로 안, 빈 공간에 대해서 진행
                        queue.append(((nx, ny), 'J'))  # queue에 해당 지점 삽입
                        graph[nx][ny] = 'J'  # 해당 미로를 지훈이로 변경
                        j_visited[nx][ny] = True  # 방문 처리
            else:  # 현재 node가 불인 경우
                for d in range(4):  # 상하좌우 탐색
                    nx, ny = cur[0][0] + dx[d], cur[0][1] + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'J') and not f_visited[nx][ny]:  # 미로 안, 빈 공간과 지훈이 위치에 대해서 진행
                        queue.append(((nx, ny), 'F'))  # queue에 해당 지점 삽입
                        graph[nx][ny] = 'F'  # 해당 미로를 불로 변경
                        f_visited[nx][ny] = True  # 방문 처리
    return False  # 다 했는데 탈출을 못했을 경우


queue = deque()
j_visited = [[False]*c for _ in range(r)]
f_visited = [[False]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            queue.append(((i, j), 'J'))  # 지훈이 정보를 항상 queue 맨 앞에 위치하도록 입력
            j_visited[i][j] = True
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            queue.append(((i, j), 'F'))  # 불 정보 입력
            f_visited[i][j] = True
possible = bfs()
if possible:
    sys.stdout.write(str(answer))
else:
    sys.stdout.write("IMPOSSIBLE")
