#Amount of time reqired for the binarytree to be infected
#BURNING TREE
def __init__(self,val=0,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right
from collections import deque
class solution:
    def amountOfTime(self,root:optional[TreeNode],start:int)->int:
        mpp={}
        q=deque([root])
        while(len(q)>0):
            node=q.popleft()
            if(node.left):
                mpp[node.left]=node
                q.append(node.left)
            if(node.right):
                mpp[node.right]=node
                q.append(node.right)
        return mpp
    def inorder(root,start):
        if(root==None):
            return None
        if(root.val==start):
            return root
        path1=inorder(root.left,start)
        if(path1!=None):
            return path1
        path2=inorder(root.right,start)
        return path1 or path2
    d=get_parent_address(root)#parent address
    startNode=inorder(root,start)
    time=0
    visited =set([statNode])
    que=deque([startNode])
    while(len(que)>0):
        for i in range(len(que)):
            node=que.popleft()
            #parent
            if(node in d and d[node]not in visited):
                visited.add(d[node])
                que.append(d[node])
            #left
            if(node.left and node.left not in visited):
                visited.add(node.left)
                que.append(node.left)
            #right
            if(node.right and node.right not in visited):
                visited.add(node.right)
                que.append(node.right)
            time+=1
        return time-1
        