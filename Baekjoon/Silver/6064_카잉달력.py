import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):  # x가 나올 수 있는 경우에 대해서 y값 대조하고, 그 최소를 구함
    m, n, x, y = map(int, input().split())
    count = x
    while count <= m * n:
        if (count - y) % n == 0:
            sys.stdout.write(str(count)+'\n')
            break
        count += m
    else:
        sys.stdout.write('-1\n')
