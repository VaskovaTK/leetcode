# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root) -> list:

        lst = []

        def inorder(root):
            if root == None:
                return
            else:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)

        inorder(root)
        return lst
    # def inorderTraversal(self, root: TreeNode) -> list:
    #     retArr = list()
    #     if root:
    #         retArr.append(root.val)
    #         returnArr = self.recursion(root,retArr)
    #         return returnArr
    #     else:
    #         return retArr
    #
    # def recursion (self,root: TreeNode, array:list):
    #     if root.left:
    #         array.append(root.left.val)
    #         self.recursion(root.left, array)
    #     if root.right:
    #         array.append(root.right.val)
    #         self.recursion(root.right,array)
    #     return array

def example(root, node2, node3, node4, node5):
    treeRoot = TreeNode(root)
    treeNode2 = TreeNode(node2)
    treeNode3 = TreeNode(node3)
    treeNode4 = TreeNode(node4)
    treeNode5 = TreeNode(node5)
    treeRoot.left = treeNode2
    treeRoot.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    return treeRoot

sol = Solution()
print(sol.inorderTraversal(example(1,2,3,4,5)))