class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        res = [0] * len(digits)

        for i in range(len(digits)):
            res[i] = digits[i]
        
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                plusVal = digits[i] + 1
            
                if plusVal < 10:
                    res[i] = plusVal
                    carry = False
                else:
                    res[i] = plusVal % 10
            else:
                break


        if carry:
            res.insert(0, 1)
        
        return res
