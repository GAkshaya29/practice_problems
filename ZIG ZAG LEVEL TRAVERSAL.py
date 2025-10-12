#ZIG ZAG LEVEL TRAVERSAL
#odd=left to right
#even=righth to left

root=list(map(int,input().split()))
from collections import deque
ans=[]
q=deque ([root])
level_count=0
while(len(q)>0):
    level=[]
    for i in range(len(q)):
        node=q.popleft()
        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)
        level.append(node.data)
    if(level_count%2==1): #odd level
        ans.append(level[::-1]) #reverse list to get right to left 
    else:
        ans.append(level)
    level_count+=1
print(ans)