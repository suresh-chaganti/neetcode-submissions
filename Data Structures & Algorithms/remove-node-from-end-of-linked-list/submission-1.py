# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        
        linked_list_len = 0
        curr = head
        while curr:
            linked_list_len = linked_list_len +1
            curr = curr.next
        
        curr = head
        index_of_elmt_tobe_rmvd = linked_list_len - n
        
        if index_of_elmt_tobe_rmvd == 0:
            return head.next
    
        for i in range(linked_list_len -1):
            if i == index_of_elmt_tobe_rmvd - 1:
                curr.next = curr.next.next
                break
            curr = curr.next 
    
        return head
