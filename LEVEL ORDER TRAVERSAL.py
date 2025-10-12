#LEVEL ORDER TRAVERSAL
#we use queue,level and ans for solving this problem
#we pop the elements in queue everytime then check for the children and add them to the queue.
#once we are done poping th element after adding the children we add the element to the level
#no.of elements in the level=no.of elements initally in the queue then we add the elemetns to the ans and empty the level
#dequeu is used to reduce the time complexity from O(n) to O(1)

from collections import deque
root=list(map(int,input().split()))
ans=[]
q=deque ([root])
while(len(q)>0):
    level=[]
    for i in range(len(q)):
        node=q.popleft()
        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)
        level.append(node.data)
    ans.append(level)

print(ans)
