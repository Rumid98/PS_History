T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_num = 0
    answer = 0

    for i in range(n-1, -1, -1):
        if nums[i] > max_num:
            max_num = nums[i]
        else:
            answer += (max_num - nums[i])
    print(f'#{test_case} {answer}')
