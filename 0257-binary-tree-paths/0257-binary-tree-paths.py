# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        self.backtrack(root, [])
        
        for idx in range(len(self.paths)):
            path = self.paths[idx]
            self.paths[idx] =  "->".join(path)
        
        return self.paths
        
    def backtrack(self, root, curr_path):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            curr_path.append(str(root.val))
            self.paths.append(curr_path.copy())
            return
        
        self.backtrack(root.left, curr_path + [str(root.val)])
        self.backtrack(root.right, curr_path + [str(root.val)])

        
        return 
        
        
