def lcm(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b


a, b = map(int, input().split())
lcm_num = lcm(max(a, b), min(a, b))
print(lcm_num * (a//lcm_num) * (b//lcm_num))
