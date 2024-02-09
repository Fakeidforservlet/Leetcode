class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #https://www.youtube.com/watch?v=nP_ns3uSh80
        #https://www.youtube.com/watch?v=wD7fs5P_MVo
        majority=nums[0]
        vote=0
        for i in nums:
            if vote==0:
                vote+=1
                majority=i
            elif i==majority:
                vote+=1
            else:
                vote-=1
        cnt=0
        for i in nums:
            if majority==i:
                cnt+=1
        if cnt>len(nums)//2:
            return majority
        return -1
        
                

        