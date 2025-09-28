class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0   
        number = 0  
        sign = 1     

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)  

            elif char in ["+", "-"]:
                result += sign * number 
                number = 0
                sign = 1 if char == "+" else -1

            elif char == "(":
                # Save current result and sign
                stack.append(result)
                stack.append(sign)
                # Reset for new expression
                result = 0
                sign = 1

            elif char == ")":
                result += sign * number
                number = 0
                result *= stack.pop()  
                result += stack.pop()  

        # Add last number
        result += sign * number
        return result

sol = Solution()
print(sol.calculate("1 + 1"))            
print(sol.calculate(" 2-1 + 2 "))          
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))