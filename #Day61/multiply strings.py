class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # Reverse both numbers for easier calculation
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(m):
            for j in range(n):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                res[i + j] += digit1 * digit2
                # Handle carry immediately
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        
        # Remove leading zeros
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        # Convert back to string
        return ''.join(str(x) for x in res[::-1])

sol = Solution()
print(sol.multiply("2","3"))
print(sol.multiply("123","456"))