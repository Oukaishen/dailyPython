class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
        	return False
        S = s+s
        S = S[1:-1]
        return s in S