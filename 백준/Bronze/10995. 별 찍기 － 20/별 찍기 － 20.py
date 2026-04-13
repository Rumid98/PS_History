import sys
input = sys.stdin.readline


n = int(input())
for i in range(n):
    if i % 2 != 0:
        print(end=' ')
    for j in range(n):
        print('*', end=' ')
    print()