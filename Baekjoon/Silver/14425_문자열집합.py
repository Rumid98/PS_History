def bin_search(str, lt, rt):
    res = False
    while lt <= rt:
        pivot = (lt + rt) // 2
        if s[pivot] == str:
            res = True
            break
        elif s[pivot] > str:
            rt = pivot - 1
        else:
            lt = pivot + 1
    return res


n, m = map(int, input().split())
s = []
answer = 0
for _ in range(n):
    s.append(input().strip())
s.sort()
for _ in range(m):
    command = input().strip()
    if bin_search(command, 0, len(s)-1):
        answer += 1
print(answer)
