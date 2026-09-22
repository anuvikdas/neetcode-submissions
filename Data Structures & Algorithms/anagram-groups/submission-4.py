class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordStruct = defaultdict(list)

        for s in strs:
            alph = [0] * 26 #represent all character occurences of a string as 0 initially then populate the array by increment the freq of that character
            for c in s:
                idx = ord(c) - ord('a')
                alph[idx] += 1
            
            wordStruct[tuple(alph)].append(s)
        
        return list(wordStruct.values())
            
