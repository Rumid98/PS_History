import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        cur_node = queue.popleft()
        for node in graph[cur_node]:
            if not visited[node[0]]:
                visited[node[0]] = True
                queue.append(node[0])
                weights[node[0]] = weights[cur_node] + node[1]


# 트리 정보 입력
for i in range(1, n + 1):
    commands = list(map(int, input().split()))  # 한 줄씩 입력 받음
    cur = commands[0]
    idx = 1
    while True:
        if commands[idx] == -1:  # -1이면 다음 줄 입력
            break
        a, b = commands[idx], commands[idx+1]
        graph[cur].append((a, b))
        idx += 2
weights = [0] * (n + 1)  # 가중치 저장 배열
visited = [False] * (n + 1)  # 방문 판단
bfs(1)
max_weight = max(weights)  # 임의 시작점으로 부터 가장 높은 가중치 합
max_index = weights.index(max_weight)  # 임의 시작점으로 부터 가장 높은 가중치 합을 가진 정점
weights = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(max_index)  # 그 점에서 새로 시작
sys.stdout.write(str(max(weights)))
