class Solution(object):
    def intersection(self, nums1, nums2):
        section=[]
        for i in nums1:
            if i in nums2:
                section.append(i)
        return set(section)
        