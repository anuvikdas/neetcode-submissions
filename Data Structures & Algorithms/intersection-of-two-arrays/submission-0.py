class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        res = []

        for num in nums1:
            set1.add(num)
        
        for num in nums2:
            if num in set1 and num not in set2:
                res.append(num)
            set2.add(num)
        
        return res