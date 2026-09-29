class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [0] * n

        #fill prefixes into res
        prefix = nums[0]
        for i in range(1, n):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        #multiply postfixes into res
        postfix = nums[n - 1]
        for i in range(n - 2, 0, -1):
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]
        
        res[0] = postfix

        return res



        