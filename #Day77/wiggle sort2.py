class Solution(object):
    def wiggleSort(self, nums):
        # Step 1: Sort the array
        sorted_nums = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2  # Middle index for splitting

        # Step 2: Fill the array from two halves in reverse order
        # Smaller half goes to even indices, larger half goes to odd indices
        left = sorted_nums[:mid][::-1]
        right = sorted_nums[mid:][::-1]

        nums[::2] = left   # Fill even indices
        nums[1::2] = right # Fill odd indices

obj = Solution()
nums1 = [1,5,1,1,6,4]
obj.wiggleSort(nums1)
print(nums1)  

nums2 = [1,3,2,2,3,1]
obj.wiggleSort(nums2)
print(nums2)  
