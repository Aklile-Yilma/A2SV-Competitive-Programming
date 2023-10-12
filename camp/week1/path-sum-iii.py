# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix = {0: 1}
        ans = 0
        
        def dfs(node, curr_sum):
            
            nonlocal ans, prefix
            
            if node == None:
                return 
            
            curr_sum += node.val
            diff = curr_sum - targetSum 
            ans += prefix.get(diff, 0) 
            print(ans, node.val)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            
            
        dfs(root, 0)
        
        return ans