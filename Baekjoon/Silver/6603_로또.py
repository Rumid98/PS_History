import itertools


while True:
    command = input().strip()
    if command == '0':
        break
    k = int(command.split()[0])
    nums = map(int, command.split()[1:])
    arr = list(itertools.combinations(nums, 6))
    for comb in arr:
        for num in comb:
            print(num, end=' ')
        print()
    print()
