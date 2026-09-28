class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = m + n - 1
        
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[ptr] = nums1[m - 1]
                m -= 1
            else:
                nums1[ptr] = nums2[n - 1]
                n -= 1
            
            ptr -= 1
        


        #the case that there are still left over (unsued nums in nums2) -- just "append" to front

        while n > 0:
            nums1[ptr] = nums2[n - 1]
            n -= 1
            ptr -=1 
