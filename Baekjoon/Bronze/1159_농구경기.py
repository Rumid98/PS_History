import sys
input = sys.stdin.readline
n = int(input())
alpha = [0] * 26
answer = ''

for _ in range(n):
    command = input().strip()
    alpha[ord(command[0]) - ord('a')] += 1
for i in range(26):
    if alpha[i] >= 5:
        answer += chr(i + ord('a'))
if answer:
    sys.stdout.write(answer)
else:
    sys.stdout.write('PREDAJA\n')
