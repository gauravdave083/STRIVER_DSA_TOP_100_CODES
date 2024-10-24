# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.


# Examples :

# Input: n = 12
# Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.

# Input: n = 2446
# Output: 1
# Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

# Input: n = 23
# Output: 0
# Explanation: 2 and 3, none of them divide 23 evenly.

#User function Template for python3


class Solution:
     def evenlyDivides (self, N):
          # code here
          count = 0
          num_str = str(N)
          
          for i in num_str:
               if int(i) == 0:
                    continue
               if N % int(i) != 0:
                    count += 1
          return count