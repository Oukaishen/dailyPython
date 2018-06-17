class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i, num in enumerate(nums):
            res^= (num^i)
        return res

if __name__ == '__main__':
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
    
