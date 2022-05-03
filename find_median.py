some_nums = [13,7,-3,82,4]
some_nums.sort()
mid = len(some_nums) // 2
res = (some_nums[mid] + some_nums[~mid]) / 2

print(res)