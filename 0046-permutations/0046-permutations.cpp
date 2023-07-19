class Solution {
public:
    void dfs(vector<int>& nums, int ind, vector<vector<int>> &res){
        if(ind == nums.size()){
            res.push_back(nums);
            return;
        }
        for(int i=ind; i < nums.size(); i++){
            swap(nums[i], nums[ind]);
            dfs(nums, ind + 1, res);
            swap(nums[i], nums[ind]);
        }    
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        dfs(nums, 0, res);
        return res;
    }
};