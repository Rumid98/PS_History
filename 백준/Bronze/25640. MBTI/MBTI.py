import sys
def input(): return sys.stdin.readline().strip()


def main():
    a = input()
    answer = 0
    for _ in range(int(input())):
        if input() == a:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()