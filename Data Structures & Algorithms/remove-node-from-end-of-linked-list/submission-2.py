# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #turtle and the hare pointer method
        dummy = ListNode(0,head)
        left = dummy
        cur = head
        while n > 0 and cur:
            cur = cur.next
            n -= 1        
        while cur:
            left = left.next
            cur = cur.next
        
        left.next = left.next.next

        return dummy.next
        