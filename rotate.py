# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     nodeHead = head
    #     rememberedNode = None
    #     countHead = head
    #     count = 1
    #     if head:
    #         while countHead.next != None:
    #             countHead = countHead.next
    #             count += 1
    #         if k>count:
    #             k=k%count
    #         while k > 0:
    #             if nodeHead.next:
    #                 while nodeHead.next != None:
    #                     if nodeHead.next.next == None:
    #                         rememberedNode = nodeHead
    #                     nodeHead = nodeHead.next
    #                 else:
    #                     nodeHead.next = head
    #                     rememberedNode.next = None
    #                 k-=1
    #                 head = nodeHead
    #             else:
    #                 return nodeHead
    #         return nodeHead
    #     else:
    #         return head
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        nodeHead = head
        firstHead = head
        count = 1
        if k == 0:
            return head
        if head:
            while firstHead.next != None:
                firstHead = firstHead.next
                count += 1
            if count == 1:
                return head
            if k>count:
                k=k%count
                if k == 0:
                    return head
                remain = count-k
            else:
                remain = count-k
            if remain == 0:
                return head
            while remain>1:
                remain-=1
                if nodeHead.next:
                    nodeHead = nodeHead.next
            else:
                headStart = nodeHead.next
                retHead = nodeHead.next
                nodeHead.next = None
            if headStart:
                while headStart.next != None:
                    headStart = headStart.next
                else:
                    headStart.next = head
                return retHead
            else:
                headStart.next = head
                return retHead
        else:
            return head




sol = Solution()
node4 = ListNode(5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
node1 = ListNode(2, node2)
head = ListNode(1, node1)

# head = ListNode(1, None)

# while head.next != None:
#     print(head.val)
#     head = head.next
# else:
#     print(head.val)

sol.rotateRight(head, 10)

# array = [1,2,3]
# k = 2000000
# m = k%3
# print(m)