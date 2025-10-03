
def canJump(nums):
    maxReach = 0
    for i in range(len(nums)):
        if i > maxReach:   # If current index is not reachable
            return False
        maxReach = max(maxReach, i + nums[i])  # Update farthest we can reach
        if maxReach >= len(nums) - 1:  # Can reach last index
            return True
    return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))