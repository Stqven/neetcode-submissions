# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        if head == None:
            return None
        prev = None

        while cur is not None:
            temp = cur.next #0, 1 
            cur.next = prev #none,
            prev = cur #0,
            cur = temp #1,

        return prev
        
         