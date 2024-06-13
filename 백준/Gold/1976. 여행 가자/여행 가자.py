import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    m = int(input())
    connect = [list(map(int, input().split())) for _ in range(n)]
    info = list(map(int, input().split()))
    parent = [i for i in range(n+1)]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    for i in range(n):
        for j in range(i+1, n):
            if connect[i][j] == 1:
                union(i+1, j+1)
    for i in range(m-1):
        if find(info[i]) != find(info[i+1]):
            print('NO')
            break
    else:
        print('YES')


if __name__ == "__main__":
    main()
