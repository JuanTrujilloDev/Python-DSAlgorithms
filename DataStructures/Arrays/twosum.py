# Input: nums = [2,7,11,15], target = 9
# Input: nums = [3,3], target = 6

def twoSum(nums, target):
    numbers = dict()
    for i in range(0, len(nums)):
        if target - nums[i] in numbers:
            return [numbers[target - nums[i]], i]
        
        numbers[nums[i]] = i

print(twoSum([2,7,11,15], 9))

