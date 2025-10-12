#floor:- Largest element in the array where element <= x
#ceil:- Smallest element in the array where element >= x
#------------------------------------------------------------------------------------------
#---------------------------------CEIL VALUE-----------------------------------------------
class Solution:
    def findCeil(self,root,x):
        ans= -1
        while(root!= None):
            if(root.data>=x):
                ans= root.data
                root=root.left
            else:
                root=root.right
        return ans
    
#--------------------------------------------------------------------------------------------
#---------------------------------FLOOR VALUE------------------------------------------------
class Solution:
    def findCeil(self,root,x):
        ans= -1
        while(root!= None):
            if(root.data>=x):
                ans= root.data
                root=root.right
            else:
                root=root.left
        return ans
#------------------------------------------------------------------------------------------