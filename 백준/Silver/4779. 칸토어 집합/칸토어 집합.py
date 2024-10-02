import sys
def input(): return sys.stdin.readline().strip()


c_set = []
def main():
    while True:
        try:
            global c_set
            n = int(input())
            c_set = ['-'] * (3**n)
            cantor(0, n)
            print(''.join(c_set))
        except EOFError:
            break
        except ValueError:
            break


def cantor(s, n):
    if n == 0:
        return
    for i in range(s + 3 ** (n - 1), s + 2 * 3 ** (n - 1)):
        c_set[i] = ' '
    cantor(s, n - 1)
    cantor(s + 3 ** (n - 1), n - 1)
    cantor(s + 2 * 3 ** (n - 1), n - 1)


if __name__ == "__main__":
    main()
