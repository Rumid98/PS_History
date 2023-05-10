import sys
input = sys.stdin.readline


# 나무의 수 n <= 1,000,000(백만) / 가져가려는 나무의 길이 m <=2,000,000,000(20억)
# 가능한 랜선의 최대 길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))
lt, rt = 1, max(trees)
while lt <= rt:
    pivot = (lt + rt) // 2
    count = 0
    for tree in trees:
        if tree > pivot:
            count += (tree - pivot)
    if count < m:
        rt = pivot - 1
    else:
        lt = pivot + 1
sys.stdout.write(str(rt))
