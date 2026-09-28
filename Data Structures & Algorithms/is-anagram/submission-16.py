class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [0] * 26
        tArr = [0] * 26
        
        for c in s:
            idx = ord(c) - ord('a')
            sArr[idx] += 1
        for c in t:
            idx = ord(c) - ord('a')
            tArr[idx] += 1

        if (sArr == tArr):
            return True
        else:
            return False