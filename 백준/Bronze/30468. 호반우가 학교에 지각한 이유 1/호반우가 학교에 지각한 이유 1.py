import sys
input = sys.stdin.readline


stats = list(map(int, input().split()))
if sum(stats[0:4]) >= stats[4]*4:
    print(0)
else:
    print(stats[4]*4 - sum(stats[0:4]))
    