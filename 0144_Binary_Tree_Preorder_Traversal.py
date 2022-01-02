# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return list()
        
        node_stack = [root]
        nodes = []
        
        while node_stack:
            root = node_stack.pop()
            
            if root:
                nodes.append(root.val)
                
                if root.right:
                    node_stack.append(root.right)
                if root.left:
                    node_stack.append(root.left)
                    
        return nodes
