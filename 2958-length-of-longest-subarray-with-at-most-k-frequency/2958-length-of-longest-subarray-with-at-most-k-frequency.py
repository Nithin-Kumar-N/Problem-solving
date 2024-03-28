class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        frequency = {}
        
        for right, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) + 1
            
            if frequency[num] > k:
                while nums[left] != num:
                    frequency[nums[left]] -= 1
                    left += 1
                frequency[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
