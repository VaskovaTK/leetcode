from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        linkedQue = deque()
        while head.next:
            linkedQue.append(head)
            head = head.next
        linkedQue.append(head)
        headNode = linkedQue.pop()
        copyHeadNode = headNode
        while len(linkedQue)>0:
            node = linkedQue.pop()
            headNode.next = node
            headNode = headNode.next
        headNode.next = None
        return copyHeadNode



def example (head, node2, node3, node4, node5):
    Node5 = ListNode(node5, None)
    Node4 = ListNode(node4, Node5)
    Node3 = ListNode(node3, Node4)
    Node2 = ListNode(node2, Node3)
    Head = ListNode(head, Node2)
    return Head


sol = Solution()
sol.reverseList(example(1,2,3,4,5))

