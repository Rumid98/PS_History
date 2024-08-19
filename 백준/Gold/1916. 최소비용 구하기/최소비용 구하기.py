import sys
def input(): return sys.stdin.readline().strip()


def main():
    INF = float("inf")
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
    start, end = map(int, input().split())
    dijkstra = [INF for _ in range(n+1)]
    visited = [False for _ in range(n + 1)]
    dijkstra[start] = 0
    while True:
        node = -1
        max_len = INF
        for i in range(1, n+1):
            if not visited[i] and dijkstra[i] < max_len:
                node, max_len = i, dijkstra[i]
        if node == -1:
            break
        for x in graph[node]:
            next_node, distance = x[0], x[1]
            if not visited[next_node]:
                dijkstra[next_node] = min(dijkstra[next_node], dijkstra[node] + distance)
        visited[node] = True
    print(dijkstra[end])


if __name__ == "__main__":
    main()
