a, b, c = map(int, input().split())
d = [0] * 81
answer = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            d[i+j+k] += 1
maxi = d[3]
for l in range(4, 81):
    if d[l] > maxi:
        answer = l
        maxi = d[l]
print(answer)
