class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def countSubarraysWithMax(max_num):
            count = 0
            window_start = 0
            max_freq = 0

            for window_end in range(len(nums)):
                if nums[window_end] == max_num:
                    max_freq += 1

                while max_freq >= k:
                    count += len(nums) - window_end
                    if nums[window_start] == max_num:
                        max_freq -= 1
                    window_start += 1

            return count

        max_num = max(nums)
        result = countSubarraysWithMax(max_num)
        return result
        