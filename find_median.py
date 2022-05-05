# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes a list of numbers and returns a median value.
##

def find_median(some_nums):
    """Takes a list of numbers and returns a median value."""
    some_nums.sort()
    if len(some_nums) % 2 == 1:
        return some_nums[len(some_nums) // 2]
    else:
        return (some_nums[len(some_nums) // 2-1] + some_nums[len(some_nums // 2)]) / 2

##some_nums = [13,7,-3,82,4]
##print(find_median(some_nums))
#