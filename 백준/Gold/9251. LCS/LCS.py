import sys
def input(): return sys.stdin.readline().strip()


def main():
    s, t = ' ' + input(), ' ' + input()
    len_s, len_t = len(s), len(t)
    dp = [[0] * len_s for _ in range(len_t)]
    for i in range(1, len_t):
        for j in range(1, len_s):
            if t[i] == s[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[len_t-1][len_s-1])


if __name__ == "__main__":
    main()
