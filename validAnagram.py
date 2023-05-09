class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        # creating a dictionary to keep track of character count in both s 
        # and t strings. both dictionaries should be same for anagrams
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0) # neat way to set or get the previous value of s[i] in the dictionary
            countT[t[i]] = 1+ countT.get(t[i],0)

            return countS == countT 
