class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates easily
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])  # move to next index since each number used once
                current.pop()
                prev = candidates[i]  # Mark previous number to skip duplicates

        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
print(sol.combinationSum2([2,5,2,1,2], 5))