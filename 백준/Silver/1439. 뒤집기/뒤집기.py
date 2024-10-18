import sys
input = sys.stdin.readline


number = input().strip()
reverse_zero, reverse_one = 0, 0
for i in range(len(number)):
    if i == 0:
        if number[i] == '1':
            reverse_one += 1
    else:
        if number[i] == '1' and number[i-1] == '0':
            reverse_one += 1
for i in range(len(number)):
    if i == 0:
        if number[i] == '0':
            reverse_zero += 1
    else:
        if number[i] == '0' and number[i-1] == '1':
            reverse_zero += 1
print(min(reverse_one, reverse_zero))
