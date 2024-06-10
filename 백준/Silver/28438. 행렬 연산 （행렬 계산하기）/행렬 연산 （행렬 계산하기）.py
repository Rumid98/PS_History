import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, m, q = map(int, input().split())
    rows, cols = [0] * n, [0] * m
    for _ in range(q):
        com, a, b = map(int, input().split())
        if com == 1:
            rows[a-1] += b
        else:
            cols[a-1] += b
    for i in range(n):
        for j in range(m):
            print(rows[i] + cols[j], end=' ')
        print()


if __name__ == "__main__":
    main()
