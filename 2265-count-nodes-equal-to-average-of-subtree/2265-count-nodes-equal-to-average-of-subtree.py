# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
            result = 0
            def helper(root, total, count):
                
                nonlocal result
                if root == None:
                    return [0, 0]
                
                if root.left == None and root.right == None:
                    result += 1
                    return [root.val, 1]
                
                left_traversal = helper(root.left, total, count)
                right_traversal = helper(root.right, total, count)
                
                num_nodes = left_traversal[1] + right_traversal[1] + 1
                total = left_traversal[0] + right_traversal[0] + root.val
                
                if root.val == (total // num_nodes):
                    result += 1
                    
                return [total, num_nodes]
            
            
            helper(root, 0, 0)
            
            return result
                    