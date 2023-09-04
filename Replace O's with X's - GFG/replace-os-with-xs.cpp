//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<vector<char>> fill(int n, int m, vector<vector<char>>& mat){
        vector<vector<int>>dont(n,vector<int>(m,1));
        vector<vector<int>>vis(n,vector<int>(m,0));
        queue<pair<int,int>>q;
        
        for(int row=0;row<n;row++)
        {
            if(mat[row][0]=='O')
            {
                q.push({row,0});
            }
            
            if(mat[row][m-1]=='O')
            {
                q.push({row,m-1});
            }
            
        }
        
        for(int col=0;col<m;col++)
        {
            if(mat[0][col]=='O')
            {
                q.push({0,col});
            }
            
            if(mat[n-1][col]=='O')
            {
                q.push({n-1,col});
            }
        }
        
        while(!q.empty())
        {
            int row=q.front().first;
            int col=q.front().second;
            dont[row][col]=0;
            q.pop();
            
            
            int roww[]={-1,0,1,0};
            int coll[]={0,1,0,-1};
            
            
            for(int i=0;i<4;i++)
            {
                int newrow=row+roww[i];
                int newcol=col+coll[i];
                
                
                if(newrow>=0 && newrow<n && newcol>=0 && newcol<m && mat[newrow][newcol]=='O' && vis[newrow][newcol]==0)
                {
                    vis[newrow][newcol]=1;
                    dont[newrow][newcol]=0;
                    q.push({newrow,newcol});
                }
            }
        }
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(dont[i][j]!=0)
                {
                    mat[i][j]='X';
                }
            }
        }
        
        return mat;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        vector<vector<char>> mat(n, vector<char>(m, '.'));
        for(int i = 0;i < n;i++)
            for(int j=0; j<m; j++)
                cin>>mat[i][j];
        
        Solution ob;
        vector<vector<char>> ans = ob.fill(n, m, mat);
        for(int i = 0;i < n;i++) {
            for(int j = 0;j < m;j++) {
                cout<<ans[i][j]<<" ";
            }
            cout<<"\n";
        }
    }
    return 0;
}
// } Driver Code Ends