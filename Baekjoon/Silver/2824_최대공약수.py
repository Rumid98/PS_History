import sys
input = sys.stdin.readline
n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))


a, b = 1, 1
for x in ns:
    a *= x
for y in ms:
    b *= y
if a > b:
    a, b = b, a
while b > 1:
    if b % a == 0:
        break
    else:
        b, a = a, b % a
len_a = len(str(a))
if len_a > 9:
    sys.stdout.write(str(a)[len_a-9:])
else:
    sys.stdout.write(str(a))




