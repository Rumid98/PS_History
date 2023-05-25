def fun(n, t):
    if t == 0:
        return n ** 2
    return fun(2*n - 1, t-1)


print(fun(2, int(input())))
