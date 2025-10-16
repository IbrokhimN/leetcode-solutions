class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        missing = -1

        for i in range(len(nums)):
            if nums[i] != i:
                missing = i
                break

        if missing == -1:
            return len(nums)
        else:
            return missing
