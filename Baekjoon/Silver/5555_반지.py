find = input().strip()
f_len = len(find)
n = int(input())
answer = 0


for i in range(n):
    command = input().strip()
    changed = False
    for j in range(10):
        if command[j] == find[0]:  # 시작 알파벳 발견
            count = 0
            idx = j
            while True:
                if count == f_len:
                    changed = True
                    answer += 1
                    break
                if find[count] != command[idx]:
                    break
                count += 1
                idx += 1
                if idx == 10:
                    idx = 0
        if changed:
            break
print(answer)
