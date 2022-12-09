from sys import stdin, stdout
input = stdin.readline
n = int(input())
scores = list(map(int, input().split()))


answer = sum(scores) * (100 / max(scores)) / n
stdout.write(str(answer))





