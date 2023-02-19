n = int(input())
a, pa, b, pb = map(int, input().split())
max = 0
answer = [0, 0]


# pa, pb의 최대 10_000_000 -> O(n)으로 해결
for i in range(n//pa + 1):
    val = a*i + b*((n-i*pa)//pb)
    if val > max:
        max = val
        answer[0], answer[1] = i, (n-i*pa)//pb
print(answer[0], answer[1])
