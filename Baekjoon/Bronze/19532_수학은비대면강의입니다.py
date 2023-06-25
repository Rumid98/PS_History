a, b, c, d, e, f = map(int, input().split())
answer = []
end = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            answer.append(x)
            answer.append(y)
            end = True
            break
    if end:
        break
print(answer[0], answer[1])
