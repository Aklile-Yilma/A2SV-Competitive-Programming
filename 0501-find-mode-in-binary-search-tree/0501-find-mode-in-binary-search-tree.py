# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root, counter):
            
            if root == None:
                return
            
            if root.val in counter:
                counter[root.val] += 1
            else:
                counter[root.val] = 1
            
            helper(root.left, counter)
            helper(root.right, counter)
            
            return counter
        
        counter = helper(root, {})
        max_value = max(counter.values())
        
        return [key for key, value in counter.items() if value == max_value]