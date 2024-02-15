class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #https://www.youtube.com/watch?v=6yOWLXlWOJc
        # currString=''
        # currNum=0
        # stack = []
        # for i in s:
        #     if i.isdigit():
        #         currNum=currNum*10+int(i)
        #     elif i=='[':
        #         stack.append((currNum,currString))
        #         currString=''
        #         currNum=0
        #     elif i==']':
        #         prevNum,prevString=stack.pop()
        #         currString=prevString+ currString*prevNum
        #     else:
        #         currString+=i
        # return currString

        #simple_one
        #https://www.youtube.com/watch?v=2CWaEsQly4o
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                subst=''
                while stack[-1]!='[':
                    subst=stack.pop()+subst
                stack.pop()
                digit=''
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                stack.append(subst*int(digit))
        print(''.join(stack))
        return ''.join(stack)
