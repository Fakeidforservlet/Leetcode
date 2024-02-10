class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #https://www.youtube.com/watch?v=t46QZYmqfoo
        # dic={}
        # for i in range(len(nums)):
        #     if nums[i] in dic and abs(i-dic[nums[i]])<=k:
        #         return True
        #     dic[nums[i]]=i
        # return False

        #https://www.youtube.com/watch?v=AyiGBwFlMb8
        num_set=set()
        for i in range(len(nums)):
            if i>k:
                num_set.remove(nums[i-k-1])
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        return False
            
