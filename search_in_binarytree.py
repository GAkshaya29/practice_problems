#Search in Binary Tree
class Solution:
    def searchBST(self,root:Optional[TreeNode]):
        while(root!=None and root.val!=val):
            if(val<root.val):
                root= root.left
            elif(val>root.val):
                root=root.right
                return root
        