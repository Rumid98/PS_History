import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
answer = ''


# 최종적으로 한 자리 숫자도 소수가 되려면, 시작 수는 2, 3, 5, 7 뿐이다.
# 그 다음 숫자들은 2의 배수가 오면 안된다. 즉, 올 수 있는 수는 1, 3, 5, 7, 9 뿐이다.
def dfs(a):
    if len(str(a)) == n:
        global answer
        answer += (str(a) + '\n')
    else:
        for y in nums2:
            if isPrime(10 * a + y):
                dfs(10 * a + y)


# 소수 판별
def isPrime(a):
    for i in range(2, a//2 + 1):
        if a % i == 0:
            return False
    return True


nums1 = [2, 3, 5, 7]
nums2 = [1, 3, 5, 7, 9]
for x in nums1:
    dfs(x)
sys.stdout.write(answer)
