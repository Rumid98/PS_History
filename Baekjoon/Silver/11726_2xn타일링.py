import sys
input = sys.stdin.readline
n = int(input())


# 2xn 타일의 가짓수
# 2x(n-1)에서 '세로로 한 개 놓는 경우' 를 양 쪽으로 두 가지
# 2x(n-2)에서 '가로로 두 개 놓는 경우' 를 양 쪽으로 두 가지
# 결국 이전 두 경우를 합한 값과 동일
D = [0] * 1001
D[1] = 1
D[2] = 2
for i in range(3, n + 1):
    D[i] = D[i-1] + D[i-2]
sys.stdout.write(str(D[n] % 10007))  # 결과를 10,007로 나눈 나머지 출력
