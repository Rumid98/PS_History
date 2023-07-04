from collections import deque
n = int(input())  # 정점 개수
info = [list(map(int, input().split())) for _ in range(n)]  # 간선 정보 배열
graph = [[] for _ in range(n+1)]  # 각 정점으로부터 이동 가능한 정점 저장
answer = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if info[i][j] == 1:  # 간선 정보인 경우
            graph[i+1].append(j+1)  # 해당 정점 -> 정점 정보 입력

for i in range(1, n+1):  # 정점 1부터 탐색
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(i)
    while queue:
        cur = queue.popleft()
        for j in range(len(graph[cur])):
            possible_node = graph[cur][j]
            if not visited[possible_node]:  # 아직 방문하지 않은 정점인 경우
                visited[possible_node] = True
                answer[i][possible_node] = 1
                queue.append(possible_node)  # 해당 정점 queue에 삽입
for i in range(1, n+1):
    for j in range(1, n+1):
        print(answer[i][j], end=' ')
    print()
