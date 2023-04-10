"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root == None:
            return 0

        depth = 0
        # print(root, depth)
        for child in root.children:
            depth = max(self.maxDepth(child), depth)

        return depth + 1
    
        
        

        