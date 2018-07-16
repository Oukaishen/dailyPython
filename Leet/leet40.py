class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.temp = []
        candidates.sort()
        self.backtrack(candidates,target,0,0)
        return self.res


    def backtrack(self, candidates, target, start, current):

        if current > target:
            return
        elif current == target:
            self.res.append(self.temp[:])

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i-1]:
                continue

            self.temp.append(candidates[i])
            self.backtrack( candidates, target, i+1, current +  candidates[i])
            self.temp.pop()

