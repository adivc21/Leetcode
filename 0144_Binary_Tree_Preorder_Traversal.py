# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # # -----x-----x-----
        # # Solution 1 - Recursion
        # # Time complexity = O(n)
        # # Space complexity = O(n)

        # if root:
        #     return ([root.val]
        #            + self.preorderTraversal(root.left)
        #            + self.preorderTraversal(root.right))
        # return []
        # # -----x-----x-----
         
        # # -----x-----x-----
        # # Solution 2 - Iteration, using stack
        # # Time complexity = O(n)
        # # Space complexity = O(2n)        

        # if not(root):
        #     return list()
        
        # node_stack = [root]
        # nodes = []
        
        # while node_stack:
        #     root = node_stack.pop()
            
        #     if root:
        #         nodes.append(root.val)
                
        #         if root.right:
        #             node_stack.append(root.right)
        #         if root.left:
        #             node_stack.append(root.left)
                    
        # return nodes
        # # -----x-----x-----

        # # -----x-----x-----
        # # Solution 3 - Iteration, using stack, condensed
        # # Time complexity = O(n)
        # # Space complexity = O(2n)    
        node = root
        res, stack = list(), list()
        
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
                
            node = stack.pop().right    
            
        return res
        # # -----x-----x-----        