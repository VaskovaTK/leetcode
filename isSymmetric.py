class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        leftArr = []
        rightArr = []
        self.recursLeft(root.left,leftArr)
        self.recursRight(root.right,rightArr)
        if rightArr == leftArr:
            return True
        else:
            return False

    def recursLeft(self, root, arr:list):
        if root:
            self.recursLeft(root.left, arr)
            arr.append(root.val)
            self.recursLeft(root.right, arr)
        arr.append(None)


    def recursRight(self, root, arr:list):
        if root:
            self.recursRight(root.right,arr)
            arr.append(root.val)
            self.recursRight(root.left,arr)
        arr.append(None)



    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root.left and root.right:
    #         firstRoot = root.left
    #         mirrorRoot = root.right
    #         flagArr = [True]
    #         self.recursion(firstRoot,mirrorRoot, flagArr)
    #         return flagArr[0]
    #     elif root.left:
    #         return False
    #     elif root.right:
    #         return False
    #     else:
    #         return True
    # def recursion (self, firstRoot, mirrorRoot, flag: list):
    #     if firstRoot.val == mirrorRoot.val:
    #         if firstRoot.left and mirrorRoot.right:
    #             if flag[0] == False:
    #                 return False
    #             self.recursion(firstRoot.left, mirrorRoot.right, flag)
    #         if firstRoot.right and mirrorRoot.left:
    #             if flag == False:
    #                 return False
    #             self.recursion(firstRoot.right, mirrorRoot.left, flag)
    #         if not firstRoot.left and not mirrorRoot.right:
    #             pass
    #         if not firstRoot.right and not mirrorRoot.left:
    #             pass
    #     else:
    #         flag[0] = False
    #         return False




def example(root, node2, node3, node4, node5,node6):
    treeRoot = TreeNode(root)
    treeNode2 = TreeNode(node2)
    treeNode3 = TreeNode(node3)
    treeNode4 = TreeNode(node4)
    treeNode5 = TreeNode(node5)
    treeNode6 = TreeNode(node6)
    # treeNode7 = TreeNode(node7)
    treeRoot.left = treeNode2
    treeRoot.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeNode6
    # treeNode3.right = treeNode7
    return treeRoot

sol = Solution()
# print(sol.isSymmetric(example(1,2,2,3,4,4,3)))
# print(sol.isSymmetric(example(2,1,2,2,2,2,3)))
# print(sol.isSymmetric(example(1,2,2,None,3,None,3)))
print(sol.isSymmetric(example(1,2,2,None,3,3)))