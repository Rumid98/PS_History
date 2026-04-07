import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(map(int, input().split())))