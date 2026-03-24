import sys
input = sys.stdin.readline


N = int(input())
plugs = [int(input()) for _ in range(N)]
print(sum(plugs) - N + 1)
