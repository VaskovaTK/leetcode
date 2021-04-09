class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxDepthArray = self.treeRecursion(root,[0],1)
        return maxDepthArray[0]

    def treeRecursion (self, root,countArray:list,count):
        if root.left is not None:
            if countArray[0]<count:
                countArray[0] = count
            self.treeRecursion (root.left, countArray, count+1)
        else:
            if countArray[0] < count:
                countArray[0] = count
        if root.right is not None:
            if countArray[0]<count:
                countArray[0] = count
            self.treeRecursion(root.right, countArray, count+1)
        else:
            if countArray[0]<count:
                countArray[0] = count
        return countArray


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

def example2(root, node2,node3,node4,node5,node6,node7):
    treeRoot = TreeNode(root)
    treeNode2 = TreeNode(node2)
    treeNode3 = TreeNode(node3)
    treeNode4 = TreeNode(node4)
    treeNode5 = TreeNode(node5)
    treeRoot6 = TreeNode(node6)
    treeRoot7 = TreeNode(node7)
    treeRoot.left = treeNode2
    treeRoot.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeRoot6
    treeNode3.right = treeRoot7
    return treeRoot

def example3 (root, node2):
    treeRoot = TreeNode(root)
    treeNode = TreeNode(node2)
    treeRoot.left =treeNode
    return treeRoot
sol = Solution()
# sol.maxDepth(example2(3,9,20,None,None,15,7))
sol.maxDepth(example3(1,2))