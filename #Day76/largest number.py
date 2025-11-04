class Solution(object):
    def largestNumber(self, nums):
        # Convert all numbers to strings for comparison
        nums = list(map(str, nums))

        # Simple bubble-sort style comparison (since we can't use cmp_to_key)
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare concatenated results
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    # Swap if needed
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # Edge case: all zeros
        if nums[0] == "0":
            return "0"

        # Join and return result
        return ''.join(nums)


# Example usage
obj = Solution()
print(obj.largestNumber([10, 2]))       
print(obj.largestNumber([3, 30, 34, 5, 9])) 