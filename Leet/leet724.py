class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums is None or len(nums) == 0:
        	return -1
        if len(nums) == 1:
        	return 0

        right = sum(nums)
        left = 0
        i = 0
        while i < len(nums):
        	if i > 0:
        		left += nums[i-1]
        	right -= nums[i]
        	if left == right:
        		return i
        	i += 1
        return -1


if __name__ == '__main__':
	print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))