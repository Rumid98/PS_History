import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x <= root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    for _ in range(m):
        command = list(map(int, input().split()))
        if command[0] == 0:  # Union
            union(command[1], command[2])
        else:  # Find
            if find(command[1]) == find(command[2]):
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    main()
