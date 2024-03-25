class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            # Get the absolute value of num
            index = abs(num)
            # If the number at index is negative, it means we've seen it before
            if nums[index - 1] < 0:
                duplicates.append(index)
            else:
                # Mark the number at index as visited by negating it
                nums[index - 1] *= -1
        
        return duplicates
