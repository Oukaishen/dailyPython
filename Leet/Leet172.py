class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # ans = 0
        # while n >= 5:
        # 	a = n//5
        # 	ans += a
        # 	n = a
        # return ans

        return sum( [n//(5**k) if (5**k <= n) else 0 for k in range(1,20)] )
 

if __name__ == '__main__':
	print(Solution().trailingZeroes(5))