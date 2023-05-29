t = int(input())
for _ in range(t):
    test_case = int(input())
    grades = list(map(int, input().split()))
    count = [0 for _ in range(101)]
    for grade in grades:
        count[grade] += 1
    max_grade = 0
    max_count = 0
    for i in range(101):
        if count[i] >= max_count:
            max_count = count[i]
            max_grade = i
    print(f'#{test_case} {max_grade}')

