from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        # Move slow one step and fast two steps until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Reset one pointer to the start
        slow = nums[0]
        
        # Move both pointers one step at a time until they meet again
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # The meeting point is the duplicate number
        return slow

# Example usage
solution = Solution()
nums = [1, 3, 4, 2, 2]
print(solution.findDuplicate(nums))  # Output should be 2
