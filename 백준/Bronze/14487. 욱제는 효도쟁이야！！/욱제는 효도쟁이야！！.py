import sys
input = sys.stdin.readline


n = int(input())
costs = list(map(int, input().split()))
print(sum(costs) - max(costs))