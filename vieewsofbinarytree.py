#TOP VIEW
from collections import deque
d={}
q=deque([root,0])
while(len(q)>0):
    node,vertical=q.popleft()
    if(node.left):
        q.append(node.left,vertical-1)
    if(node.right):
        q.append(node.right,vertical+1)
    if(vertical not in d):
        d[vertical]=node.data
    ans=[]
    for i in sorted(d):
        ans.append(d[i])
    print ans
 #------------------------------------------------------------------------------   
#BOTTOM VIEW
from collections import deque
d={}
q=deque([root,0])
while(len(q)>0):
    node,vertical=q.popleft()
    if(node.left):
        q.append(node.left,vertical-1)
    if(node.right):
        q.append(node.right,vertical+1)
    d[vertical]=node.data
    ans=[]
    for i in sorted(d):
        ans.append(d[i])
    print ans
#---------------------------------------------------------------------------------  
#LEFT SIDE VIEW
from collections import deque
d={}
q=deque([root,0])
while(len(q)>0):
    node,vertical=q.popleft()
    if(node.left):
        q.append(node.left,vertical-1)
    if(node.right):
        q.append(node.right,vertical+1)
    if(vertical not in d):
        d[vertical]=node.data
    ans=[]
    for i in sorted(d):
        ans.append(d[i] 0)
    print ans
#------------------------------------------------------------------------------------
#RIGHT SIDE VIEW
from collections import deque
d={}
q=deque([root,0])
while(len(q)>0):
    node,vertical=q.popleft()
    if(node.left):
        q.append(node.left,vertical-1)
    if(node.right):
        q.append(node.right,vertical+1)
    d[vertical]=node.data
    ans=[]
    for i in sorted(d):
        ans.append(d[i] -1)
    print ans