from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # n: 유저의 수, m: 친구 관계의 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    count = 1
    while queue:
        loop_len = len(queue)  # 한 번 건너갈 때마다 단계가 +되는 것 계산하기 위해
        for _ in range(loop_len):
            cur = queue.popleft()
            for x in graph[cur]:  # 현재 node에서 갈 수 있는 모든 node 계산
                if not visited[x]:
                    visited[x] = True
                    queue.append(x)
                    steps[v][x] = count
        count += 1


steps = [[0 for _ in range(n+1)] for _ in range(n+1)]  # 1~n명이므로 0을 제외한 1~n index 사용
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    bfs(i)
minimum_step = sum(steps[1])
minimum_person = 1
for i in range(1, n+1):
    tmp = sum(steps[i])
    if tmp < minimum_step:
        minimum_step = tmp
        minimum_person = i
print(minimum_person)
