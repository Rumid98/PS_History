import sys
def input(): return sys.stdin.readline().strip()


def main():
    nums = [input() for _ in range(3)]
    print(int(nums[0]) + int(nums[1]) - int(nums[2]))
    print(int(nums[0] + nums[1]) - int(nums[2]))


if __name__ == "__main__":
    main()
