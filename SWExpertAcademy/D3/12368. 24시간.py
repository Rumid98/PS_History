T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    answer.append(f'#{test_case} {(a+b) % 24}')
print('\n'.join(answer))
