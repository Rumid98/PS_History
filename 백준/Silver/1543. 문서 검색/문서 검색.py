import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    t = input()
    idx = 0
    count = 0
    while idx != len(s):
        if s[idx] == t[0]:
            for i in range(len(t)):
                if idx + i >= len(s) or s[idx+i] != t[i]:
                    break
            else:
                count += 1
                idx += len(t)
                continue
        idx += 1
    print(count)


if __name__ == "__main__":
    main()
