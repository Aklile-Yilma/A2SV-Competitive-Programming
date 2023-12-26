# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = [] 
        
        def helper(root, isRoot):
            
            nonlocal forest
            if not root:
                return
            
            if root.val in to_delete:
                helper(root.left, True)
                helper(root.right, True)
            else:
                if root.left:
                    if root.left.val in to_delete:
                        helper(root.left, True)
                        root.left = None
                    else:
                        helper(root.left, False)
                
                if root.right:
                    if root.right.val in to_delete:
                        helper(root.right, True)
                        root.right = None
                    else:
                        helper(root.right, False)
                
                if isRoot:
                    forest.append(root)
                
        helper(root, True)
                
        return forest
                
            