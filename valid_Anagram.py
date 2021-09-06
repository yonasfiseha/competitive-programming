#https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        str1 = sorted(s)
        str2 = sorted(t)
        if str1 != str2:
            return 0
        for i in range(len(str1)):
                if str2[i] != str1[i]:
                    return 0        
        return 1
        