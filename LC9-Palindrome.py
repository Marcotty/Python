'''
Given an integer x, return true if x is a
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
'''
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        j=len(string)
        result = False
        for c in range(len(string)):
            if string[c] == string[j-1]:
                result = True
            j-=1
            
        return result
    #FollowUp
    def isPalindromeInteger(self, x:int) -> bool:
        if x < 0: return False
        digits = int(math.log10(x))+1
        l = []
        for d in range(digits):
            single = x%10
            x = int(x/10)
            l.append(single)
        lr = l[::-1]
        print(lr)
        if l == lr:
            return True
        return False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print("#####################")
print(s.isPalindromeInteger(121))
print(s.isPalindromeInteger(-121))
print(s.isPalindromeInteger(10))