n, k = map(int, input().split())
a = []
for i in range(1, n+1):
    if n % i == 0:
        a.append(i)
print(a[k-1]) if len(a) >= k else print(0)
