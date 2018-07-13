class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
        	return 0

        NegativeSign = (dividend <0 ) is not (divisor <0)

        dividend, divisor = abs(dividend), abs(divisor)

        res = 0

        while dividend >= divisor:
        	temp, k = divisor, 1
        	while dividend >= temp:
        		dividend -= temp
        		res += k
        		temp <<= 1
        		k <<= 1

        if NegativeSign:
        	res = -res
        return min(max(res, -2147483648),2147483647)



