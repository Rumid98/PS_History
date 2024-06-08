import sys
def input(): return sys.stdin.readline().strip()


def main():
    dp = [0] * 10_001
    dp[1], dp[2], dp[3] = 1, 2, 3
    for i in range(4, 10_001):
        dp[i] = dp[i-3] + (i-2)//2 + 2
    t = int(input())
    for _ in range(t):
        print(dp[int(input())])


if __name__ == "__main__":
    main()
