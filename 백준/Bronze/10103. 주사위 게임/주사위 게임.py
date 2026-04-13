import sys
input = sys.stdin.readline


n = int(input())
A, B = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        A -= b
    elif b < a:
        B -= a
        
print(A)
print(B)