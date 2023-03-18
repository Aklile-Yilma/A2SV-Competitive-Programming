# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = defaultdict(int)
        count[0] = 1
        self.result = 0
        
        def backtrack(root, total):
            
            if root == None:
                return
            
            total += root.val            
            self.result += count[total - targetSum]
            
            #count
            count[total] += 1
            
            backtrack(root.left, total)            
            backtrack(root.right, total)
            
            count[total] -= 1
            
            
        backtrack(root, 0)
        
        return self.result