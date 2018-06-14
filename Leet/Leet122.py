class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
        return sum( (prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0 for i in range(1, len(prices) ) ) )

if __name__ == '__main__':
	input = [7,1,5,3,6,4]
	print(Solution().maxProfit(input)) 