# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum-=root.val
        if not root.right and not root.left:
            return sum==0
        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
