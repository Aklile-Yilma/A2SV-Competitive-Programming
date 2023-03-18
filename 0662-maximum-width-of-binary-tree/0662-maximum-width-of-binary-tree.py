# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            
        width = 1
        curr_level = [(root, 1)]
        
        while curr_level:
            next_level = []
            for node, pos in curr_level:
                if node.left:
                    next_level.append((node.left, 2*(pos)))
                if node.right:
                    next_level.append((node.right, 2*(pos)+1))

            if next_level:
                width = max(width, next_level[-1][1] - next_level[0][1] + 1)
                
            curr_level = next_level
        
        return width
    
        