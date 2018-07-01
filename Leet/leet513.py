from TreeNode import TreeNode

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        
        while len(queue) > 0:
        	node = queue.pop(0)
        	if node.right is not None:
        		queue.append(node.right)
        	if node.left is not None:
        		queue.append(node.left)

        return node.val

        """
        通过改变思维，先右后左，可以自然地使用最后一个变量的位置，无需记录下来。
        """