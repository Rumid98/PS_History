n = int(input())
r = []
c = []
for _ in range(n):
    x, y = map(int, input().split())
    r.append(x)
    c.append(y)
print((max(r)-min(r)) * (max(c)-min(c)))
