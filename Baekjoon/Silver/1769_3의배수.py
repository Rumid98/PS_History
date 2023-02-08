x = int(input())
count = 0
while len(str(x)) > 1:
    tmp = 0
    for i in str(x):
        tmp += int(i)
    x = tmp
    count += 1
print(count)
if x % 3 == 0:
    print('YES')
else:
    print('NO')
