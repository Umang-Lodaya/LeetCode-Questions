//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    bool DFS(int node,vector<int>&vis,vector<int>&path,

                 vector<int>&check,vector<int> adj[])
  {
      vis[node]=1;
      path[node]=1;
      
      for(auto it:adj[node])
      {
          if(!vis[it])
          {
              if(DFS(it,vis,path,check,adj))
              {
                  return true;
              }
              
          }
          else if(path[it]==1)return true;
      }
      
      check[node]=1;
      path[node]=0;
      return false;
  }
  public:
    vector<int> eventualSafeNodes(int V, vector<int> adj[]) {
        // code here
        vector<int>vis(V,0),path(V,0),check(V,0),safeNodes;
        for(int i=0;i<V;i++)
        {
            if(!vis[i]) DFS(i,vis,path,check,adj);
        }
        for(int i=0;i<V;i++)
        {
            if(check[i]==1)safeNodes.push_back(i);
        }
        return safeNodes;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {

        int V, E;
        cin >> V >> E;
        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
        }

        Solution obj;
        vector<int> safeNodes = obj.eventualSafeNodes(V, adj);
        for (auto i : safeNodes) {
            cout << i << " ";
        }
        cout << endl;
    }
}

// } Driver Code Ends