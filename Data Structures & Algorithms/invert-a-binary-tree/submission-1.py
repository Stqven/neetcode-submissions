# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        res = self.swtich_children(root)

        return res



    

    def swtich_children(self, root):
        if(root is None):
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.swtich_children(root.left)
        self.swtich_children(root.right)

        return root