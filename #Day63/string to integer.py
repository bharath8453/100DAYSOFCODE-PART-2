class Solution(object):
    def myAtoi(self, s):
        # Step 1: Ignore leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Convert digits
        num = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            num = num * 10 + digit
            index += 1

        # Step 4: Apply sign
        num *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

s = "42"
print(Solution().myAtoi(s)) 

s = "   -042"
print(Solution().myAtoi(s))  

s = "1337c0d3"
print(Solution().myAtoi(s))  

s = "0-1"
print(Solution().myAtoi(s)) 

s = "words and 987"
print(Solution().myAtoi(s))