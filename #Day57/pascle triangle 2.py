class Solution(object):
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            # Update from right to left to avoid overwriting values we still need
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row

sol = Solution()
print(sol.getRow(3))
print(sol.getRow(0))  
print(sol.getRow(1)) 