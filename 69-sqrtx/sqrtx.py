class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=1
        while (ans * ans)<x:
            ans+=1
        if (ans * ans)==x:
            return ans
        else:
            return ans-1
        