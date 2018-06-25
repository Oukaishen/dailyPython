class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

       	length = max(len(v1), len(v2))

       	for i in range(length):
       		num1 =  int(v1[i]) if i < len(v1) else 0
       		num2 =  int(v2[i]) if i < len(v2) else 0

       		if num1 < num2:
       			return -1
       		elif num1 > num2:
       			return 1

       	return 0



if __name__ == '__main__':
	print("1.2.3.4".split("."))