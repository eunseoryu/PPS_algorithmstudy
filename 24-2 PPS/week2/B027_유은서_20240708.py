# problem url: https://leetcode.com/problems/middle-of-the-linked-list/
# rabbit & turtle algorithm: https://medium.com/@k1ckap0l03/rabbit-and-turtle-algorithm-2c68dde598a2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabit = head
        turtle = head

        while rabit is not None and rabit.next is not None:
            turtle = turtle.next
            rabit = rabit.next.next
        
        return turtle