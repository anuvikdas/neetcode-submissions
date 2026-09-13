'''
Questions:
-Are we dealing with the case that 'x' and 'X' are equivalent?
-We are just returning the length and not the actual string, correct?

Brute Force:
-For each possible start to a string, so for each character we can compute the longest substring that can be made from that character's position by maintaining a seen set for all the characters in that window and then when a repeat occurs we mark the length and then on to the next character. This is complexity; however, would be O(n^2) and a space complexity of O(m * n). 

Optimal Approach:
-Instead of checking for each character, we can just sequentially pass through the string maintaining a sliding window approach. We expand our right pointer and if we incur a repeated character (deemed by a general seen set) then we shrink our window by moving our left pointer, and mark that window's size. We then return the largest window size, which would be our largest substring w/o repeating characters. Our time complexity in this case would be O(n) for our one pass and our memory complexity would be O(n) for our seen set. 

Dry Run:
-In the case of s = "zyxzxyz", we would start at z and add it to our seen set, and then move our right pointer one. Then we would do the same until we reach index 3. We see that we have a z here and because it already is in our set. We take the window length and compare it to res, if it is bigger we replace it. Then we shrink our window by incrementing our left pointer so that it points so index 1. 


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        seen = set()
        l = 0
        r = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res

