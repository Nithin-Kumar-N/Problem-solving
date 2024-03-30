class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
    
private:
    int atMostK(vector<int>& nums, int k) {
        vector<int> count(nums.size() + 1, 0);
        int distinct = 0;
        int left = 0;
        int result = 0;
        
        for (int right = 0; right < nums.size(); ++right) {
            if (count[nums[right]] == 0)
                distinct++;
            count[nums[right]]++;
            
            while (distinct > k) {
                count[nums[left]]--;
                if (count[nums[left]] == 0)
                    distinct--;
                left++;
            }
            
            result += right - left + 1;
        }
        
        return result;
    }
};