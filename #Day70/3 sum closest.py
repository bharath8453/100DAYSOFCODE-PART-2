class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        # Initialize closest with the sum of the first three elements
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if current_sum is nearer to target
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match found
                    return current_sum
        
        return closest

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1)) 
print(s.threeSumClosest([0,0,0], 1))