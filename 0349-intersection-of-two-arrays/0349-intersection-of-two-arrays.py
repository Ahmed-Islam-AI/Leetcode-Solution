class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #first converting list into a sets

        set1 = set(nums1)
        set2 = set(nums2)
        
        #returning the intersection of the two sets

        return list(set1 & set2)
        