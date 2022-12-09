from sys import stdin, stdout
input = stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = ''


sums = [0] * 100001
for i in range(len(numbers)):
    sums[i+1] = sums[i] + numbers[i]
for _ in range(m):
    a, b = map(int, input().split())
    stdout.write(str(sums[b] - sums[a-1]) + '\n')
