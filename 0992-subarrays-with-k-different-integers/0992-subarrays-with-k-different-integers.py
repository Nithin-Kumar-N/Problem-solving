class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = [0] * (len(nums) + 1)
            distinct = 0
            left = 0
            result = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                
                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                
                result += right - left + 1
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)