# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        paths = []

        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                # Leaf node reached, append the path to paths
                paths.append(path[::-1])  # Reverse the path
                return
            if node.left:
                dfs(node.left, path + chr(node.left.val + ord('a')))
            if node.right:
                dfs(node.right, path + chr(node.right.val + ord('a')))

        dfs(root, chr(root.val + ord('a')))  # Start DFS from the root with the root's value

        # Sort paths lexicographically and return the smallest one
        return min(paths)   