T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    avg = sum(nums) // n
    for num in nums:
        if num <= avg:
            count += 1
    answer.append(f'#{test_case} {count}')
print('\n'.join(answer))
