class Solution {
private:
    int findMaxAmount(int curr_house, vector<int>& nums, vector<int>& dp) {
        int n = nums.size();
        if(curr_house >= n) return 0;
        if(dp[curr_house] != -1) return dp[curr_house];
    
        int not_rob = findMaxAmount(curr_house + 1, nums, dp);
        int rob = max(not_rob, nums[curr_house] + findMaxAmount(curr_house + 2, nums, dp));
    
        return dp[curr_house] = max(rob, not_rob);
    }

public:
     int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        if(n == 2) return max(nums[0], nums[1]);
    
        vector<int> dp (n + 1, -1);
        return findMaxAmount(0, nums, dp);
    }
};