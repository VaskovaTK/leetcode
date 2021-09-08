# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        from collections import deque
        copyHead = head
        copyHead2 = head
        firstQueue = deque()
        secondQueue = deque()
        while copyHead.next:
            firstQueue.appendleft(copyHead.val)
            copyHead = copyHead.next
        firstQueue.appendleft(copyHead.val)
        while copyHead2.next:
            secondQueue.append(copyHead2.val)
            copyHead2 = copyHead2.next
        secondQueue.append(copyHead2.val)
        while len(firstQueue)>0:
            first = firstQueue.pop()
            second = secondQueue.pop()
            if first == second:
                continue
            else:
                return False
        return True

        # firstHead = head
        # newFirstHead = None
        # if head.next:
        #     secondHead = head.next
        # else:
        #     return True
        # while head.next:
        #     if head.next.next:
        #         head = head.next
        #     else:
        #         newFirstHead = head.next
        #         head.next = None
        #         break
        # if newFirstHead.val == firstHead.val:
        #     newFirstHead.next = secondHead
        #     if newFirstHead.next:
        #         newFirstHead = newFirstHead.next
        #         firstHead = firstHead.next
        #     else:
        #         return True
        # else:
        #     return False
        # while newFirstHead.next:
        #     if firstHead:
        #         if firstHead.val == newFirstHead.val:
        #             newFirstHead = newFirstHead.next
        #             firstHead = firstHead.next
        #         else:
        #             return False
        #     else:
        #         break
        # return True



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
        # print(retHead)
    return retHead

sol = Solution()
print(sol.isPalindrome(example([1,2,2,1])))
print(sol.isPalindrome(example([1,2,3])))
print(sol.isPalindrome(example([0,0])))
print(sol.isPalindrome(example([1,1,2,1])))
# сломалось на примере [0,0]