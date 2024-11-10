import sys
input = sys.stdin.readline


n = int(input())
for i in range(1, n+1):
    words = list(input().split())
    print(f'Case #{i}:', end=' ')
    for w in words[::-1]:
        print(w, end=' ')
    print()