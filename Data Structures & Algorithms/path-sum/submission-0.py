# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        _sum = 0
        def dfs(root, _sum) -> int:
            if not root:
                return False
            
            _sum = _sum + root.val

            if root.left == None and root.right == None:
                return _sum == targetSum

            return (dfs(root.left, _sum) or dfs(root.right, _sum))
        return dfs(root, _sum)
            