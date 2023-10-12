# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            
        ans = float('inf')

        def dfs(node):

            nonlocal ans
            if node == None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if (left and right) or ((node.val == p.val or node.val == q.val) and (left or right)):
                if ans == float('inf'):
                    ans = node

                return True
            
            
            if node.val == p.val or node.val == q.val:
                return True

            return left or right

        dfs(root)
        return ans