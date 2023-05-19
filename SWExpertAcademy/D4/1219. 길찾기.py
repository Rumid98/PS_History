def dfs(v):
    if v == 99:  # 도착
        return True
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            visited[graph[v][i]] = True
            if dfs(graph[v][i]):
                return True
    return False


for _ in range(10):
    test_case, n = map(int, input().split())
    commands = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [False for _ in range(100)]  # 방문 판단 배열
    for i in range(len(commands) // 2):  # node 연결 정보 입력
        graph[commands[2*i]].append(commands[2*i + 1])
    if dfs(0):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
