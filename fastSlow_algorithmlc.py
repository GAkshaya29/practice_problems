classNode:
def __init__(self,data):
    self.val = data
    self.next = None
def CreateLinkedList(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next