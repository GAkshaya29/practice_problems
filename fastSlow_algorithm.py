head= list(map(int,input().split()))
slow= head
fast= head
while(fast!=None and fast.next !=None):
    slow= slow.next
    fast= fast.next.next
print(slow)