# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# Constraints:

# -231 <= x <= 231 - 1







class Solution:
     def reverse(self, x: int) -> int:
          # Example walkthrough with x = -123
          
          # Step 1: Check if the input number is negative
          # For x = -123, is_negative will be True
          is_negative = x < 0
          
          # Step 2: Convert number to positive and then to string
          # abs(-123) = 123
          # str(123) = "123"
          num_str = str(abs(x))
          
          # Step 3: Reverse the string using string slicing
          # "123"[::-1] = "321"
          # [::-1] means start:end:step, where -1 step means reverse direction
          reversed_num_str = num_str[::-1]
          
          # Step 4: Remove any leading negative signs (if present)
          # This is a safety measure, though in this case it's not needed
          # as we handled the sign separately
          reversed_num_str = reversed_num_str.lstrip('-')
          
          # Step 5: Convert the reversed string back to integer
          # int("321") = 321
          reversed_num = int(reversed_num_str)
          
          # Step 6: If original number was negative, make result negative
          # If is_negative is True: 321 becomes -321
          if is_negative:
               reversed_num = -reversed_num
          
          # Step 7: Check if result is within 32-bit integer range
          # 32-bit range is [-2³¹, 2³¹ - 1] = [-2147483648, 2147483647]
          if -2**31 <= reversed_num <= 2**31 - 1:
               return reversed_num  # Return result if within range
          else:
               return 0  # Return 0 if result is out of range