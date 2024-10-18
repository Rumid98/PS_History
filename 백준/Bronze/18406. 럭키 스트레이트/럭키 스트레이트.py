import sys
input = sys.stdin.readline


n = input().strip()
sum_left, sum_right = 0, 0
for i in range(len(n)//2):
    sum_left += int(n[i])
    sum_right += int(n[-1-i])
print('LUCKY') if sum_left == sum_right else print('READY')
