class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
        	return False
        dupx = x
        rev = 0
        while x:
        	rev = rev * 10 + x%10
        	x //= 10
        return rev == dupx

if __name__ == '__main__':
	print( Solution().isPalindrome(121) )
