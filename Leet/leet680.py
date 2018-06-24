class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1
        while(i < j):
        	if s[i] != s[j]:
        		return self.helper(s,i+1,j) or self.helper(s, i, j-1)
        	i += 1
        	j -= 1
        return True


    def helper(self, s, i, j):
    	"""
    	s:str
    	i: low index
    	j: high index
    	"""
    	while(i < j):
    		if s[i] != s[j]:
    			return False
    		i += 1
    		j -= 1
    	return True