# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverse_LL(self,middle_element_pt):
        prev_node=None
        current_node=middle_element_pt
        while current_node:
            front_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=front_node
        return prev_node
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle_element_pt=self.findMiddle(head)
        after_middle_element_head=self.reverse_LL(middle_element_pt)
        middle_element_pt=None
        current_node=head
        while current_node and after_middle_element_head:
            if current_node.val!=after_middle_element_head.val:
                return False
            current_node=current_node.next 
            after_middle_element_head=after_middle_element_head.next
        return True


        
#Using stack
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     stack=[]
    #     current_node=head
    #     while current_node:
    #         stack.append(current_node.val)
    #         current_node=current_node.next
    #     current_node=head
    #     while current_node:
    #         top_element=stack.pop()
    #         if current_node.val!=top_element:
    #             print('not a palindrome')
    #             return False
    #         current_node=current_node.next
    #     return True
            