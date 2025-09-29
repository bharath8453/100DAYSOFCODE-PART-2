class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill the middle values if row > 2
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result

sol = Solution()
print(sol.generate(5)) 
print(sol.generate(1)) 
