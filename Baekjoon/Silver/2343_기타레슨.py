import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))


# 최대 약 30번의 bin_search로 결과 도출 가능
def bin_search1(t):  # t: target blue_lay volume
    answer = 100000*10000
    s, e = max(nums), 100000*10000
    while s <= e:
        p = (s + e) // 2
        count = 0  # 블루레이 개수
        tmp = 0  # 강의 길이 합
        for i in range(n):
            if tmp + nums[i] > p:  # 블루레이 한도 초과 시
                tmp = 0  # 다음 블루레이로 넘기고, 초기화
                count += 1  # 블루레이 개수 증가
            tmp += nums[i]
        if tmp:  # 잔여 강의 존재
            count += 1
        if count > t:
            s = p + 1
        else:
            e = p - 1
            answer = p
    return answer


sys.stdout.write(str(bin_search1(m)))
