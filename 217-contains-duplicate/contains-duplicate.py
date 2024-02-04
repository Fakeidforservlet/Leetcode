class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
                if dic[i]>1:
                    return True
            else:
                dic[i]=1
        return False
            
        