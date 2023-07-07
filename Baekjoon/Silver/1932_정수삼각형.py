n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]  # 삼각형 숫자 정보 배열
dp = [[0 for _ in range(i)] for i in range(1, n+1)]  # dp 배열
dp[0][0] = graph[0][0]  # 시작은 반드시 graph[0][0](첫 번째 수)
for i in range(1, n):  # 층
    for j in range(i+1):  # i층의 숫자들
        if j == 0:  # 맨 왼쪽인 경우
            dp[i][j] = dp[i-1][j] + graph[i][j]
        elif j == i:  # 맨 오른쪽인 경우
            dp[i][j] = dp[i-1][j-1] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])
print(max(dp[n-1]))
