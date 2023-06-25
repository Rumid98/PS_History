def lcm(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b


a, b = map(int, input().split())
c, d = map(int, input().split())
final_a = a*d + b*c
final_b = b * d
final_lcm = lcm(max(final_a, final_b), min(final_a, final_b))
print((final_a//final_lcm), (final_b//final_lcm))
