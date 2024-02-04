class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # ans=1
        # while (ans * ans)<x:
        #     ans+=1
        # if (ans * ans)==x:
        #     return ans
        # else:
        #     return ans-1

        #https://www.youtube.com/watch?v=Bsv3FPUX_BA

        low=1
        high=x
        result = 0
        while low<=high:
            mid=low+(high-low)//2
            if (mid*mid)<=x:
                result = mid
                low=mid+1
            else:
                high=mid-1
        return result
        