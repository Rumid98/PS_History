a = ['L', 'O', 'V', 'E']
name = input().strip()
answer = []
n = int(input())


def check(str1, str2):
    for x in str1:
        if x == a[0]:
            count[0] += 1
        elif x == a[1]:
            count[1] += 1
        elif x == a[2]:
            count[2] += 1
        elif x == a[3]:
            count[3] += 1
    for x in str2:
        if x == a[0]:
            count[0] += 1
        elif x == a[1]:
            count[1] += 1
        elif x == a[2]:
            count[2] += 1
        elif x == a[3]:
            count[3] += 1


for i in range(n):
    count = [0, 0, 0, 0]
    command = input().strip()
    check(name, command)
    pro = ((count[0]+count[1]) * (count[0]+count[2]) * (count[0]+count[3]) * (count[1]+count[2]) * (count[1]+count[3]) * (count[2]+count[3])) % 100
    answer.append((pro, command))
answer.sort(key=lambda x: x[1], reverse=True)
answer.sort(key=lambda x: x[0])
print(answer[n-1][1])
