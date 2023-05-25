nums = sorted(list(map(int, input().split())))
print(2 * (nums[0] + nums[1]) - 1) if nums[0] + nums[1] <= nums[2] else print(sum(nums))
