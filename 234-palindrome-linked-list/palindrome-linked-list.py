# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        current_node=head
        while current_node:
            stack.append(current_node.val)
            current_node=current_node.next
        current_node=head
        while current_node:
            top_element=stack.pop()
            if current_node.val!=top_element:
                print('not a palindrome')
                return False
            current_node=current_node.next
        return True
            