# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #Determine if root exists
        if not root:
            return 0
        
        #Create a queue and start by passing it the root
        queue = deque([root])

        #Create a variable to hold sum
        Sum = 0

        #while loop continues while queue has values, values will be removed in process
        while queue:
            #remove element on left side
            element = queue.popleft()

            #Check if element has left child and add to queue
            if element.left:
                queue.append(element.left)
                #Determine if left node of element has children
                if not element.left.left and not element.left.right:
                    Sum += element.left.val
            
            #Check if element has right child and add if so
            if element.right:
                queue.append(element.right)

        return Sum
