class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #https://www.youtube.com/watch?v=t46QZYmqfoo
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic and abs(i-dic[nums[i]])<=k:
                return True
            dic[nums[i]]=i
        return False
