# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        
        def backtrack(root, total, curr_path):
            
            if root == None:
                return
            
            if root.left == None and root.right == None:
                total += root.val
                curr_path.append(root.val)
                if total == targetSum:
                    paths.append(curr_path)        
                return
            
            backtrack(root.left, total + root.val, curr_path + [root.val])
            backtrack(root.right, total + root.val, curr_path + [root.val])
            
            return
        
        backtrack(root, 0, [])
        
        return paths