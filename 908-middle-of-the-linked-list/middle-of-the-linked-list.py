# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # listLength = 1

        # currNode = head
        # currNodeVal = head.val
        # currNodeNext = head.next

        # while currNodeNext is not None:
        #     listLength += 1
        #     currNodeVal = currNodeNext.val
        #     currNodeNext = currNodeNext.next
        
        # for i in range(listLength//2):
        #     currNode = currNode.next

        # return currNode

        middleNode = head
        endNode = head

        while endNode is not None and endNode.next is not None:
            middleNode = middleNode.next
            endNode = endNode.next.next

        return middleNode