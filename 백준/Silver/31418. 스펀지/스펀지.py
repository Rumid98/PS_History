import sys
def input(): return sys.stdin.readline().strip()


def main():
    w, h, k, t = map(int, input().split())
    virus = [list(map(int, input().split())) for _ in range(k)]
    virus_area = [0] * k
    answer = 1
    for i in range(k):
        x, y = virus[i]
        lx = t if x - t > 0 else x - 1
        rx = t if x + t <= w else w - x
        ly = t if y - t > 0 else y - 1
        ry = t if y + t <= h else h - y
        virus_area[i] = (lx + rx + 1) * (ly + ry + 1) % 998_244_353
    for a in virus_area:
        answer = answer * a % 998_244_353
    print(answer)


if __name__ == "__main__":
    main()
