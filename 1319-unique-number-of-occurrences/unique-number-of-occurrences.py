class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #https://www.youtube.com/watch?v=b2_rw2NZkr8
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return len(dic)==len(set(dic.values()))
