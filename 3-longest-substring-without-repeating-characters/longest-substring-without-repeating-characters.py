class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #https://www.youtube.com/watch?v=qtVh-XEpsJo
        max_len=0
        left=right=0
        num_set=set()
        sub_len=0
        while right<len(s) and left<=right:
            if s[right] not in num_set:
                num_set.add(s[right])
                right+=1
                sub_len+=1
            else:
                num_set.remove(s[left])
                left+=1
                sub_len-=1
            if sub_len>max_len:
                max_len=sub_len
        return max_len