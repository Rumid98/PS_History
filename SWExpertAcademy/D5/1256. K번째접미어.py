T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    word = input().strip()
    word_len = len(word)
    suffix_arr = []
    for i in range(word_len):
        suffix_arr.append(word[i:word_len])
    suffix_arr.sort()
    print(f'#{test_case} {suffix_arr[n-1]}')
