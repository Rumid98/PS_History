t = list(map(int, input().split()))

while t[0] != 0 and t[1] != 0 and t[2] != 0:
    t = sorted(t)
    if t[0] + t[1] <= t[2]:
        print('Invalid')
    else:
        if t[0] == t[1] == t[2]:
            print('Equilateral')
        elif t[0] == t[1] or t[1] == t[2]:
            print('Isosceles')
        else:
            print('Scalene')
    t = list(map(int, input().split()))
