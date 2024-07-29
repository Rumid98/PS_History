import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    if 200 <= n < 206: print(1)
    elif 206 <= n < 218: print(2)
    elif 218 <= n < 229: print(3)
    elif 229 <= n: print(4)

if __name__ == "__main__":
    main()
