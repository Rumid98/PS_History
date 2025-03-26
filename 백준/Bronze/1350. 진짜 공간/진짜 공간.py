import sys
input = sys.stdin.readline


n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
answer = 0

for file in files:
    if file:
        a, b = file//cluster, file%cluster
        if b > 0:
            answer += (a+1)
        else:
            answer += a
print(answer*cluster)
