class Solution(object):
    def grayCode(self, n):
        result = []
        total = 1 << n   # 2^n
        for i in range(total):
            result.append(i ^ (i >> 1))
        return result

sol = Solution()
print(sol.grayCode(2)) 
print(sol.grayCode(1)) 
print(sol.grayCode(3)) 