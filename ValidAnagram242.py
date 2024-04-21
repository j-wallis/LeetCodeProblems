class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if they are not same length which makes it false
        if len(s) != len(t):
            return False
        
        #Create empty hash tables for count of letters in each string
        countS, countT = {}, {}

        for i in range(len(s)):
            #Counting how many of each character in s and t
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        #iterate through all keys
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True
