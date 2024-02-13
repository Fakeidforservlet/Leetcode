class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #https://www.youtube.com/watch?v=vTlVtLvPQo4
        if len(s)<2:return s
        def expandAroundOrbit(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        longestPalindromeString=''
        for i in range(len(s)):
            oddPalindromeString=expandAroundOrbit(i,i)
            if len(oddPalindromeString)>len(longestPalindromeString):
                longestPalindromeString=oddPalindromeString
            evenPalindromeString=expandAroundOrbit(i,i+1)
            if len(evenPalindromeString)>len(longestPalindromeString):
                longestPalindromeString=evenPalindromeString
        return longestPalindromeString