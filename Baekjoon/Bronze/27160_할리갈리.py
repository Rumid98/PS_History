import sys
input = sys.stdin.readline
n = int(input())
fruits = [0, 0, 0, 0]


for i in range(n):
    command, count = input().strip().split()
    if command == 'STRAWBERRY':
        fruits[0] += int(count)
    elif command == 'BANANA':
        fruits[1] += int(count)
    elif command == 'LIME':
        fruits[2] += int(count)
    else:
        fruits[3] += int(count)
for i in range(4):
    if fruits[i] == 5:
        sys.stdout.write('YES\n')
        break
else:
    sys.stdout.write('NO\n')
