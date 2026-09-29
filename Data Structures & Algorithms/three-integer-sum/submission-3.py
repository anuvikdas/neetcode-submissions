class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: 
                return res
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            
            l, r = i + 1, n - 1
            while l < r:
                tSum = a + nums[l] + nums[r]
                if tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
        
        return res
                