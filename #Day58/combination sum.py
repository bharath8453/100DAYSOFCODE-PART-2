class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, current, total):
            # Base case: if total matches target, add the combination
            if total == target:
                result.append(list(current))
                return
            # If total exceeds target, stop exploring
            if total > target:
                return

            # Explore choices
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # we can reuse the same number, pass 'i' not 'i+1'
                backtrack(i, current, total + candidates[i])
                # Undo the choice (backtrack)
                current.pop()
        
        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7)) 
print(sol.combinationSum([2,3,5], 8))  
print(sol.combinationSum([2], 1))    