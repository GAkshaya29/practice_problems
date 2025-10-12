def isleafNode(root):
    if(root.left==None and root.right==None):
        return True
    return False
def addLeafNodes(root,result):
    curr=root.left
    while(curr):
        if(isleafNode(curr)==False):
            result.append(curr.data)
            if(curr.left):
                curr=curr.left
            else:
                curr=curr.right #curr=None
def addLeafNodes(root,result):
    if(isLeafNode(root)==True):
        result.append(root.data)
        return
    if(root.left):
        addLeafNodes(root.left,result)
    if(root.right):
        addLeafNodes(root.right,result)
def addRightNodes(root,result):
    temp=[]
    curr=root.right
    while(curr):
        if(isleafNode(curr)==False):
            temp.append(curr.data)
        if(curr.right):
            curr=curr.right
        else:
            curr=curr.left
    result.extend(temp[::-1])
if(isleafNode(root)):
    return [root.data]
result=[]
result.append(root.data)
addLeafNodes(root,result)
addLeafNodes(root,result)
addRightNodes(root,result)
return result