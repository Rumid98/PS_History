import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    info = list(map(int, input().split()))
    party = [list(map(int, input().split())) for _ in range(m)]
    parent = [i for i in range(n+1)]
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

    if info[0] == 0:
        print(len(party))
    else:
        info[1:] = sorted(info[1:])
        for i in range(info[0]):
            for j in range(info[0]):
                if i != j:
                    union(info[i+1], info[j+1])
        for p in party:
            if p[0] > 1:
                for i in range(p[0]-1):
                    union(p[i+1], p[i+2])
        root = find(info[1])
        for p in party:
            for node in p[1:]:
                if find(node) == root:
                    break
            else:
                answer += 1
        print(answer)


if __name__ == "__main__":
    main()
