import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
answer = 0

cols = [0] * n
diag1 = [0] * (2 * n - 1)
diag2 = [0] * (2 * n - 1)

def DFS(row):
    global answer
    if row == n:
        answer += 1
        return
    for col in range(n):
        if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
            continue
        cols[col] = diag1[row + col] = diag2[row - col + n - 1] = 1
        DFS(row + 1)
        cols[col] = diag1[row + col] = diag2[row - col + n - 1] = 0

DFS(0)
print(answer)
