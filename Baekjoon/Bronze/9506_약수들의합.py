n = int(input())
while n != -1:
    res = []
    tmp = 0
    answer = ''
    for i in range(1, n//2 + 1):
        if n % i == 0:
            res.append(str(i))
            tmp += i
    if tmp == n:
        print(f'{n} = ' + ' + '.join(res))
    else:
        print(f'{n} is NOT perfect.')
    n = int(input())
