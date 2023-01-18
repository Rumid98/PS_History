import sys
input = sys.stdin.readline
n = int(input())


for i in range(n):
    command = input().strip()
    count = 0
    result = 1
    for j in range(len(command) // 2):
        if command[j] != command[len(command) - j - 1]:
            count += 1
            result = 0
            break
        count += 1
    if result == 1:
        sys.stdout.write(f'{result} {count + 1}\n')
    else:
        sys.stdout.write(f'{result} {count}\n')
