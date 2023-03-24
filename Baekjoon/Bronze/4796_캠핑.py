count = 1
l, p, v = map(int, input().split())
while l != 0 and p != 0 and v != 0:
    a = v // p
    b = v % p
    print(f'Case {count}: {l*a+b}' if b <= l else f'Case {count}: {l*(a+1)}')
    count += 1
    l, p, v = map(int, input().split())
