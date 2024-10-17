import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
pq_diff = p - q
answer = []

if pq_diff == 0:
    for i in range(n):
        if A[i] != B[i]:
            print("NO")
            break
    else:
        print("YES")
        for _ in range(n):
            print(0, end=' ')
else:
    for i in range(n):
        ab_diff = A[i] - B[i]
        if ab_diff == 0:
            answer.append(0)
        else:
            if -ab_diff / pq_diff > 0 and ab_diff % pq_diff == 0:
                answer.append(-ab_diff // pq_diff)
            else:
                print("NO")
                break
    else:
        print("YES")
        for x in answer:
            print(x, end=' ')
