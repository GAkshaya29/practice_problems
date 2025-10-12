#yoyo
class Solution:
    def dfs(self,adj):
        def depth_first_search(node,vis,adj,ans):
            ans.append(node)
            for i in adj[node]:
                if(vis[i]==0):
                    vis[i]= 1
                    depth_first_search(i,vis,adj,ans)
        n= len(adj)
        vis=[0]*n
        startNode= 0
        vis[startNode]= 1
        ans=[]
        depth_first_search(startNode,vis,adj,ans)
        return ans