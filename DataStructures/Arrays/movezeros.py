def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)-1
    i = 0
    while i < n:
        if nums[i] == 0:
            num = nums.pop(i)
            nums.append(num)
            n -= 1
        else:
            i+=1

    print(nums)


moveZeroes([0,0,1])