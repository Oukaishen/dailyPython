class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum( [1 if c in J else 0 for c in S] )

if __name__ == '__main__':
	J = "aA"
	S = "aAAbbbb"
	print(Solution().numJewelsInStones(J,S))