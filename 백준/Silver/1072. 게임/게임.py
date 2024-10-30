import sys
input = sys.stdin.readline


x, y = map(int, input().split())
z = y * 100 // x
if z >= 99:
    print(-1)
else:
    answer = 0
    lx, rx = 1, 1_000_000_000
    while lx <= rx:
        pivot = (lx + rx) // 2
        nz = (y+pivot) * 100 // (x+pivot)
        if nz > z:
            answer = pivot
            rx = pivot - 1
        else:
            lx = pivot + 1
    print(answer)
