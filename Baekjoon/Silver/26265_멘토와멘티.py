import sys
input = sys.stdin.readline
n = int(input())
mentoring = [list(input().strip().split()) for _ in range(n)]


mentoring.sort(key=lambda x: x[1], reverse=True)
mentoring.sort(key=lambda x: x[0])
for i in range(n):
    sys.stdout.write(mentoring[i][0] + ' ' + mentoring[i][1] + '\n')
