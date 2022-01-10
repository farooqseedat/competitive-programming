# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left = right
            node.right = left

        return root
