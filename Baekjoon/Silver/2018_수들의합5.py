import sys
input = sys.stdin.readline
n = int(input())
answer = 0


# sliding window로 풀이(lt와 rt를 이동시키면서 해결하는 방법)
lt, rt, total = 1, 1, 1  # 초기값 설정
while lt <= rt <= n:
    if total == n:
        answer += 1
        lt += 1
        rt += 1
        total = total - lt + rt + 1
    elif total <= n:
        rt += 1
        total += rt
    else:
        total -= lt
        lt += 1
sys.stdout.write(str(answer))
