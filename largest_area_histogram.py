def findNSE(heights):
    n=len(heights)
    ans=[0]*n
    stack=[]
    for i in range(n-1,-1,-1):
        currEle=heights[i]
        while(len(stack)!=0 and heights[stack[-1]]>=currEle):
            stack.pop()
        if(len(stack)==0):
            ans[i]=n
        else:
            ans[i]=stack[-1]
        stack.append(i)
    return ans
def findPSE(heights):
     n=len(heights)
     ans=[0]*n
     stack=[]
     for i in range(0,n):
        currEle=heights[i]
        while(len(stack)!=0 and heights[stack[-1]]>=currEle):
            stack.pop()
        if(len(stack)==0):
            ans[i]=n
        else:
            ans[i]=stack[-1]
        stack.append(i)
     return ans
heights=list(map(int(input().split())))
