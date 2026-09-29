class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        head, tail = 0, n - 1

        while head <= tail:
            cand = numbers[head] + numbers[tail]

            if cand == target:
                return [head + 1, tail + 1] 
            elif cand < target:
                head += 1
            else:
                tail -= 1
        
        