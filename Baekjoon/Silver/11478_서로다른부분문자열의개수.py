s = input()
res = []
for i in range(1, len(s)+1):  # 단어 길이
    for j in range(len(s)-i+1):  # rt 범위
        res.append(s[j:j+i])
print(len(set(res)))


