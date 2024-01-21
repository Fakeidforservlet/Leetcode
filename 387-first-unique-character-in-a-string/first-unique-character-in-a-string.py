class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for i in s:
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]+=1
        for i in s:
            if frequency[i]==1:
                return s.index(i)
        return -1
        