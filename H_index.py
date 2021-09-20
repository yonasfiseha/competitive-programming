# https://leetcode.com/problems/h-index/submissions/
class Solution(object):
    def hIndex(self, citations):
        ln =len(citations)
        citations.sort()
        for i, n in enumerate(citations):
            h_index = ln - i
            if h_index <= n:
                return h_index
           
        return 0
Solution =Solution()
print('H-index is: ', Solution.hIndex([3,0,6,1,5]))