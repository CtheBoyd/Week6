# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes a list of numbers and returns a median value.
#


some_nums = [13,7,-3,82,4]
some_nums.sort()
mid = len(some_nums) // 2
res = (some_nums[mid] + some_nums[~mid]) / 2

print(res)