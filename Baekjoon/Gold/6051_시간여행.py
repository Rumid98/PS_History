import sys
import copy
input = sys.stdin.readline


query = [[] for _ in range(80_001)]
n = int(input())
for i in range(n):
    queue = copy.deepcopy(query[i])
    command = input().strip()
    if command[0] == 'a':
        queue.append(command[2:])
        query[i+1] = copy.deepcopy(queue)
    elif command[0] == 's':
        queue.pop()
        query[i+1] = copy.deepcopy(queue)
    else:
        query[i+1] = copy.deepcopy(query[int(command[2:])-1])
    if query[i+1]:
        sys.stdout.write(str(query[i+1][-1])+'\n')
    else:
        sys.stdout.write('-1\n')
