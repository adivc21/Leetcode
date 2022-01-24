# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # # -----x-----x-----
        # # Solution 1 - Recursion, using List extend and append
        # # Time complexity = O(n)
        # # Space complexity = O(n)
        
        # res = list()
        
        # if root:
        #     res.extend(self.inorderTraversal(root.left))
        #     res.append(root.val)
        #     res.extend(self.inorderTraversal(root.right))
        #     return res
        
        # return []
        # # -----x-----x-----

    
        # # -----x-----x-----
        # # Solution 2 - Recursion
        # # Time complexity = O(n)
        # # Space complexity = O(n)
        
        # if root:
        #     return (self.inorderTraversal(root.left)
        #     + [root.val]
        #     + self.inorderTraversal(root.right))
        # return []
        # # -----x-----x-----

        # # -----x-----x-----
        # # Solution 3 - Iteration, using stack
        # # Time complexity = O(n)
        # # Space complexity = O(2n)        
        
        node = root
        res, stack = list(), list()
        
        while node or stack:
            while(node):
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            res.append(node.val)
            node = node.right
            
        return res
        # # -----x-----x-----