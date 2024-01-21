class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2,0,-1):
            newstr=''
            if len(s)%i==0:
                times=len(s)//i
                while times:
                    newstr+=s[:i]
                    times-=1
            if newstr==s:
                return True
        return False
#https://www.youtube.com/watch?v=7J8x0XudV0Y