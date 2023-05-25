z = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
     'U', 'V', 'W', 'X', 'Y', 'Z']


n, b = map(int, input().split())
answer = ''
tmp = []
while n // b != 0:
    tmp.append(n % b)
    n = n // b
if n != 0:
    tmp.append(n)

for i in range(len(tmp)-1, -1, -1):
    answer += z[int(tmp[i])]
print(answer)
