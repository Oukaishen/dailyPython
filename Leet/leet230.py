class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.count = 0
        self.res = -1
        self.inorderfind(root)
        return self.res

    def inorderfind(self, root):
    	if not root:
    		return
    	self.inorderfind(root.left)

    	self.count += 1
    	if self.count == self.k:
    		self.res = root.val

    	self.inorderfind(root.right)
