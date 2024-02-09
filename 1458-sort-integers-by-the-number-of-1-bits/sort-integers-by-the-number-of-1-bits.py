#https://www.youtube.com/watch?v=2owpaafBIgw
class Solution(object):
    def count_one_bit(self,num):
        count=0
        while num:
            count+= num & 1
            num>>=1
        return count
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def custom_sort(num):
            return self.count_one_bit(num),num
        arr.sort(key=custom_sort)
        #print(arr)
        return arr

        
        