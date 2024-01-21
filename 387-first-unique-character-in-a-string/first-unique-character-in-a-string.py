class Solution:
    #using dic:
    ''' 
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
    '''

    #using array
    def firstUniqChar(self, s: str) -> int:
        char_count=[0]*256

        for i in s:
            char_count[ord(i)]+=1
        for i in s:
            if char_count[ord(i)]==1:
                return s.index(i)
        return -1
        