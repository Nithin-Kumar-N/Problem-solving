# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       def distributeCoins(self, root, pre=None):
        if not root: return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre: pre.val += root.val - 1
        return res + abs(root.val - 1)
        