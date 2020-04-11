# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #print(root)
        if(root==None):
            return 0
        left_side = self.height(root.left)
        right_side = self.height(root.right)
        
        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)
        return max(left_side+right_side,max(left_dia,right_dia))
        
    def height(self,root):
        if(root == None):
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))