sr=int(input())
sc=int(input())
color=int(input())
image=[[1,0,1],[1,1,0],[0,1,1]]
if(image[sr][sc]==color):
    print(image)
def dfs(sr,sc,image,n,m):
    for r,c in [[1,0],[-1,0],[0,1],[0,-1]]:
        ur= sr + r
        uc= sc + c
        if(ur>=0 and ur<n and uc>=0 and uc<m and image[ur][uc]==num):
            image[ur][uc]=color
            dfs(ur,uc,image,n,m)
n=len(image)
m=len(image[0])
num=image[sr][sc]
image[sr][sc]=color
dfs(sr,sc,image,n,m)
print(image)