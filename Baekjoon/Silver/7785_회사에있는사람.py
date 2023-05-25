def bin_search(name, lt, rt):
    while lt <= rt:
        pivot = (lt + rt) // 2
        if enter[pivot] == name:
            del enter[pivot]
            break
        elif enter[pivot] > name:
            rt = pivot - 1
        else:
            lt = pivot + 1


n = int(input())
enter, leave = [], []
answer = 0
for _ in range(n):
    command = list(input().split())
    if command[1] == 'enter':
        enter.append(command[0])
    else:
        leave.append(command[0])
enter.sort()
for i in range(len(leave)):
    bin_search(leave[i], 0, len(enter)-1)
print('\n'.join(sorted(enter, reverse=True)))
