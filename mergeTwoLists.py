# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        remList = None
        retList = ListNode(-1000)
        flagL1 = False
        flagL2 = False
        while True:
            if flagL1 == True and flagL2 == True:
                break
            if l1:
                if l2:
                    if l1.val<=l2.val:
                        if retList.val == -1000:
                            retList = l1
                            remList = retList
                            if l1.next:
                                l1 = l1.next
                            else:
                                l1 = None
                                flagL1 = True
                        else:
                            retList.next = l1
                            if l1.next:
                                l1 = l1.next
                            else:
                                l1 =None
                                flagL1 =True
                            retList = retList.next
                    elif l1.val>l2.val:
                        if retList.val == -1000:
                            retList = l2
                            remList = retList
                            if l2.next:
                                l2 = l2.next
                            else:
                                l2 = None
                                flagL2 = True
                        else:
                            retList.next = l2
                            retList = retList.next
                            if l2.next:
                                l2 = l2.next
                            else:
                                l2 =None
                                flagL2 = True
                else:
                    if retList.val == -1000:
                        return l1
                    else:
                        retList.next = l1
                        return remList
            elif l2:
                if retList.val == -1000:
                    return l2
                else:
                    retList.next = l2
                    return remList
            else:
                return remList
        return remList


def example (arr: list):
    head = ListNode(0)
    retHead = None
    for i in range(0, len(arr)):
        if head.val == 0:
            head.val = arr[i]
            retHead = head
        else:
            head.next = ListNode(arr[i])
            head = head.next
        print(retHead)
    return retHead


sol = Solution()
sol.mergeTwoLists(example([1,2,5]),example([3,4,6]))