# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node):
            if node == None:
                return 0

            cur = node.val if low <= node.val <= high else 0

            left = helper(node.left)
            right = helper(node.right)

            return cur + left + right

        return helper(root)