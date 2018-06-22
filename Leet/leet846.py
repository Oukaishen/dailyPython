class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if hand is None or len(hand) % W != 0:
        	return False;
        c = collections.Counter(hand)
        for i in sorted(c):
        	if c[i] > 0 :
        		for j in range(W-1, -1, -1):
        			if c[i+j] < c[i]:
        				return False
        			c[i+j] -= c[i]
        return True