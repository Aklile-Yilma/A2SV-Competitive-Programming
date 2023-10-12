# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        
        def dfs(node, cands, total):
            nonlocal paths
            
            if node == None:
                return False
            
            if node.right == None and node.left == None:
                total += node.val
                cands.append(node.val)
                if total == targetSum:
                    paths.append(cands.copy())
                    return True
            
            dfs(node.right, cands + [node.val], total + node.val)
            dfs(node.left, cands + [node.val], total + node.val)
           
        dfs(root, [], 0)
        return paths
                
            