# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = prehead = ListNode(-101, head)
        cur = head
        '''
        1 -> 1 -> 1 -> 2 -> 2 -> 3-> 3-> 4
    pre                         cur  
                      prev

        1 ->      2 -> 3 -> 3
                            
                              cur
        '''
        while cur:
            while cur and cur.val == prev.val:
                prev.next = cur.next                
                cur = cur.next
            prev = cur
            if cur:
                cur = cur.next
        return prehead.next