#leetcode 179 just see it
"""
from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d=defaultdict(int)
        for i in range(len(edges)):
            d[edges[i][0]]= d[edges[i][0]]+1
            d[edges[i][1]]= d[edges[i][1]]+1
        maxx=0
        c=0
        for i in dict(sorted(d.items(), key=lambda item: item[1])):
            maxx=max(maxx,d[i])
            c=i
    
        return c
        #dict(sorted(d.items(), key=lambda item: item[1])) sorted dictionary by values
        # remenber we can just loop through this dictionary can not be sorted
"""