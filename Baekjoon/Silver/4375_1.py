while True:
    try:
        n = int(input())
    except:
        break
    tmp = 1
    while True:  # 1부터 11, 111 .. 순으로 증가시켜보면서 나누어 떨어지는지 구해본다
        if tmp % n == 0:
            print(len(str(tmp)))
            break
        else:
            tmp = tmp*10 + 1
