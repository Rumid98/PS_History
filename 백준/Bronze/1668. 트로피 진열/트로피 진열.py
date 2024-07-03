import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    info = [int(input()) for _ in range(n)]
    left, right = 0, 0
    left_max, right_max = 0, 0
    for i in range(n):
        if info[i] > left_max:
            left += 1
            left_max = info[i]
        if info[n-i-1] > right_max:
            right += 1
            right_max = info[n-i-1]
    print(left)
    print(right)
        
    

if __name__ == "__main__":
    main()
