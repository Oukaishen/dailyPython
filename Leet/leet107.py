from TreeNode import TreeNode

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        queue = []

        if root is None:
        	return res

        queue.append(root)
        queue.append(None)

        while len(queue) > 1:
        	node = queue.pop(0)
        	if node is None:
        		res.insert(0,temp)
        		temp = []
        		queue.append(None)
        		continue
        	if node.left is not None:
        		queue.append(node.left)
        	if node.right is not None:
        		queue.append(node.right)
        	temp.append(node.val)

        res.insert(0,temp)

        return res

if __name__ == '__main__':
	