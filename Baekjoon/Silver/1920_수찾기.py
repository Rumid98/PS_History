import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))


def bin_search(s, e, t):  # s: start, e: end, t: target
    while s <= e:
        pivot = (s + e) // 2
        if t == nums[pivot]:
            sys.stdout.write("1\n")
            break
        elif t > nums[pivot]:  # target이 pivot보다 오른쪽
            s = pivot + 1
        else:  # target이 pivot보다 왼쪽
            e = pivot - 1
    else:
        sys.stdout.write("0\n")
    return


nums.sort()  # 이진탐색을 위해 수 배열 정렬
for x in finds:
    bin_search(0, n-1, x)
