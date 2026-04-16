# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        start, end = 0, len(nodes)-1
        while start < end:
            nodes[start].next = nodes[end]
            start = start + 1
            if start >= end:
                break
            nodes[end].next = nodes[start]
            end = end -1 
        
        nodes[start].next = None

        