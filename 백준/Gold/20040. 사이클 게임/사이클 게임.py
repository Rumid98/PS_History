import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(m)]
    parent = [i for i in range(n)]
    answer = 0

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

    for i in range(m):
        a, b = info[i]
        if find(a) == find(b):
            answer = i+1
            break
        union(a, b)
    print(answer)


if __name__ == "__main__":
    main()
