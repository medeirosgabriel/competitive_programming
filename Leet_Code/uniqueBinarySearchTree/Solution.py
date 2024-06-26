# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def genRootList(self, left, right):
        if (left > right): return [None]
        if (left == right): return [TreeNode(left)]
        allTrees = []
        for i in range(left, right + 1):
            leftTree = self.genRootList(left, i - 1)
            rightTree = self.genRootList(i + 1, right)
            for lRoot in leftTree:
                for rRoot in rightTree:
                    allTrees.append(TreeNode(val=i, left=lRoot, right=rRoot))
        return allTrees

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.genRootList(1, n)
