from sys import stdin, stdout
input = stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0


sums = [0] * (n+1)  # 합 배열
info = [0] * m  # 나머지 배열
for i in range(1, n+1):  # 합 배열 저장
    sums[i] = sums[i-1] + nums[i-1]
for i in range(1, n+1):  # 합 배열을 m으로 나눈 나머지 값으로 update
    sums[i] %= m
for i in range(1, n+1):  # 0 ~ m까지 나머지의 개수 count
    info[sums[i] % m] += 1
for i in range(m):
    if info[i] >= 2:
        answer += int((info[i]) * (info[i]-1) / 2)  # nC2 계산
stdout.write(str(info[0]+answer))
