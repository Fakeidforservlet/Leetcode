# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge_sorted_LL(self,left_sorted_LL,right_sorted_LL):
        current_node=dummy_node=ListNode()
        while left_sorted_LL and right_sorted_LL:
            if left_sorted_LL.val < right_sorted_LL.val:
                current_node.next=left_sorted_LL
                current_node=current_node.next
                left_sorted_LL=left_sorted_LL.next
            else:
                current_node.next=right_sorted_LL
                current_node=current_node.next
                right_sorted_LL=right_sorted_LL.next
        if left_sorted_LL:
            current_node.next=left_sorted_LL   
        elif right_sorted_LL :
            current_node.next=right_sorted_LL 
        return dummy_node.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle_element=Solution.findMiddle(head)
        left_LL_head=head
        right_LL_head=middle_element.next
        middle_element.next=None
        left_sorted_LL=self.sortList(left_LL_head)
        right_sorted_LL=self.sortList(right_LL_head)
        return self.merge_sorted_LL(left_sorted_LL,right_sorted_LL)


        