import sys
input = sys.stdin.readline


def main():
    n = int(input())
    for _ in range(n):
        tmp = list(map(int, input().split()))
        t, nums = tmp[0], tmp[1:]
        answer = 0
        for i in range(19, -1, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    answer += 1
        print(t, answer)


if __name__ == "__main__":
    main()
