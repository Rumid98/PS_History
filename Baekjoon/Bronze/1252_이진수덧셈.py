a, b = input().split()
a, b = '0b'+a, '0b'+b
print(str(bin(int(a, 2) + int(b, 2)))[2:])
