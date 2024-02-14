class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #https://www.youtube.com/watch?v=6yOWLXlWOJc
        currString=''
        currNum=0
        stack = []
        for i in s:
            if i.isdigit():
                currNum=currNum*10+int(i)
            elif i=='[':
                stack.append((currNum,currString))
                currString=''
                currNum=0
            elif i==']':
                prevNum,prevString=stack.pop()
                currString=prevString+ currString*prevNum
            else:
                currString+=i
        return currString