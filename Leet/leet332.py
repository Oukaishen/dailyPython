class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        ## use collections.defaultdict()
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
        	targets[a] += b,  ## this comma is quite important, means that it is (b,) instead of a iterable
        route, stack = [], ["JFK"]
        while stack:    ### this equals len(stack) > 0 https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
        	while targets[stack[-1]]:
        		stack += targets[stack[-1]].pop(),
        	route.insert(0, stack.pop(),)

        return route