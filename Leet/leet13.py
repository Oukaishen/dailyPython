class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numberMap = {};
        numberMap["I"] = 1
        numberMap["V"] = 5
        numberMap["X"] = 10
        numberMap["L"] = 50
        numberMap["C"] = 100
        numberMap["D"] = 500
        numberMap["M"] = 1000

        j = 1
        res = 0
        while j < len(s):
        	if numberMap[s[j-1]] < numberMap[s[j]]:
        		res -= numberMap[s[j-1]]
        	else:
        		res += numberMap[s[j-1]]
        	j += 1
        res += numberMap[s[j-1]]
        return res

if __name__ == '__main__':
	print( Solution().romanToInt("MCMXCIV"))