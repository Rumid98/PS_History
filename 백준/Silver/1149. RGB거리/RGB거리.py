import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    RGB = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = RGB[0][0], RGB[0][1], RGB[0][2]
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][j]
            if j == 1:
                dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][j]
            if j == 2:
                dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][j]
    print(min(dp[n-1]))   
    

if __name__ == "__main__":
    main()
