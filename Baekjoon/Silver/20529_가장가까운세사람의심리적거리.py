import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):  # test case 만큼 loop
    answer = 100
    n = int(input())
    MBTI = list(input().split())
    if n > 32:
        print(0)
    else:
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    tmp = 0
                    for l in range(4):
                        if MBTI[i][l] != MBTI[j][l]:
                            tmp += 1
                        if MBTI[j][l] != MBTI[k][l]:
                            tmp += 1
                        if MBTI[k][l] != MBTI[i][l]:
                            tmp += 1
                    answer = min(answer, tmp)
        print(answer)
