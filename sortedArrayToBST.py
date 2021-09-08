# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list):
        def recur(l, r):
            if l > r or l < 0 or r >= len(nums):
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])

            node.left = recur(l, mid - 1)
            node.right = recur(mid + 1, r)

            return node

        return recur(0, len(nums) - 1)