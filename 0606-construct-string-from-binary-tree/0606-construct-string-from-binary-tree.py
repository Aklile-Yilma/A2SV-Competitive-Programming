# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = []
        
        def helper(root):
            if root == None:
                return

            answer.append("(")
            answer.append(f'{root.val}')
            
            if not root.left and root.right:
                answer.append("()")
                
            helper(root.left)
            helper(root.right)
            
            answer.append(")")
        
            return 
        
        helper(root)

        return "".join(answer)[1:-1]
         