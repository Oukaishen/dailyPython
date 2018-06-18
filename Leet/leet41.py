class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
        	if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i+1:
        		i += 1
        	elif nums[ nums[i] - 1 ] != nums[i]:
        		self.swap(nums, i, nums[i] -1 )
        	else:
        		i += 1
        i = 0
        while i < len(nums) and nums[i] == i+1:
        	i +=1
        return i+1



    def swap(self, nums, i, j):
    	if i != j:
    		nums[i] ^= nums[j]
    		nums[j] ^= nums[i]
    		nums[i] ^= nums[j]

if __name__ == '__main__':
	print(Solution().firstMissingPositive([7,8,9,11,12]))