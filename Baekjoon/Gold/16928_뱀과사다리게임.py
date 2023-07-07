from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(101)]  # 사다리와 뱀 정보
for i in range(n+m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(v):
    queue = deque()
    visited = [False for _ in range(101)]
    count = 0
    found = False
    queue.append(v)
    visited[v] = True
    while queue:
        loop = len(queue)
        for _ in range(loop):
            cur_node = queue.popleft()
            if cur_node == 100:
                found = True
                break
            for i in range(1, 7):
                next_node = cur_node + i
                if 0<next_node<=100 and not visited[next_node]:  # 숫자 범위 안인지 판단
                    visited[next_node] = True
                    if graph[next_node]:  # 사다리나 뱀이 존재하는 경우
                        visited[graph[next_node][0]] = True
                        queue.append(graph[next_node][0])
                    else:  # 그 외의 경우
                        queue.append(next_node)
        if found:
            break
        count += 1
    return count

print(bfs(1))



