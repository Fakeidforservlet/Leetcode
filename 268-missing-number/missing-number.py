class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(1,len(nums)+1):
        #     if 0 not in nums:
        #         return 0
        #     elif i not in nums:
        #         return i
        arr_len=len(nums)
        total_sum=arr_len*(arr_len+1)//2
        return total_sum-sum(nums)