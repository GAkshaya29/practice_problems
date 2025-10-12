class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def createBST(arr):
    root=None
    for data in arr:
        if(root == None):
            root = Node(data)
        else:
            curr = root
            while(True):
                if(data<curr.data):
                    if(curr.left=None):
                        curr.left=Node(data)
                        break
                    else:
                        curr = curr.left
                elif(data>curr.data):
                    if(curr.right == None):
                        curr.right = Node(data)
                        break
                    else:
                        curr=curr.right
    print(root.left.data)#4
    print(root.right.left.left.right.data)#9
arr=list(map(int,input().split()))
createBST(arr)#5 13 10 7 9 4