
import math

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small = math.inf
        big = math.inf
        for num in nums:
        	if num <= small:
        		small = num
        	elif num <= big:
        		big = num
        	else:
        		return True
        return False

if __name__ == '__main__':
	print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
