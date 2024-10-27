import sys
input = sys.stdin.readline


dp = [0] * 191_230
mod = 1000000007
dp[1], dp[2] = 1, 2
for i in range(3, 191_230):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
