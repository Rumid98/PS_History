import sys
def input(): return sys.stdin.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        s, p = input().split()
        idx = 0
        count = 0
        while idx != len(s):
            if s[idx] == p[0]:
                for i in range(len(p)):
                    if idx + i >= len(s) or s[idx+i] != p[i]:
                        break
                else:
                    count += 1
                    idx += len(p)
                    continue
            idx += 1
        print(len(s) - count * (len(p) - 1))


if __name__ == "__main__":
    main()
