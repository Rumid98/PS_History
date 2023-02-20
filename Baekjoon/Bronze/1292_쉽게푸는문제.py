d = [0 for _ in range(10001)]
idx = 1
for i in range(1, 51):
    tmp = 0
    while tmp < i:
        d[idx] = d[idx-1] + i
        idx += 1
        tmp += 1
a, b = map(int, input().split())
print(d[b] - d[a-1])
