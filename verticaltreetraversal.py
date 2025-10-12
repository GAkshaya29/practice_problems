from collections import defaultdict,deque
class solution:  
    def vrticalTraversal(self,root:Optional[TreeNode]):
        q=deque([(root,0,0)])
        d=defaultdict(lambda : defaultdict(list))
        while(len(q)>0):
            node,vertical,level=q.popleft()
            if(node.left):
                q.append((node.left,vertical-1,level+1))
            if(node.right):
                q.append((node.right,vertical+1,level+1))
            d[vertical][level].append(node.val)
        result=[]
        #we have a dict inside a dict 
        #first for loop is to acess the first dict to get teh keys
        for i in sorted (d): #only keys will be sorted not the values when we use sorted(d)
            col=[]
            #we use the second for loop to acess the dict within the dict to get the keys
            for j in sorted (dict[i]):
                col.extend(sorted d[i][j]) #over here we take the values and append them into the col
            result.append(col)
        return result