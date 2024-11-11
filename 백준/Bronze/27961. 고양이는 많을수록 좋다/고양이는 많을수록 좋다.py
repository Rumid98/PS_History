import sys
input = sys.stdin.readline


n = int(input())
if n == 0:
    print(0)
else:
    count = 0
    while True:
        if 2 ** (count-1) < n <= 2 ** count:
            break
        count += 1
    print(count+1)