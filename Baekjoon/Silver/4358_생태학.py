import sys
input = sys.stdin.readline
dic = {}
total = 0


while True:
    command = input().strip()
    if command == '':
        break
    if command in dic:
        dic[command] += 1
    else:
        dic[command] = 1
    total += 1
trees = sorted(list(dic.keys()))
for tree in trees:
    print(f'%s %.4f' %(tree, 100*dic[tree]/total))
