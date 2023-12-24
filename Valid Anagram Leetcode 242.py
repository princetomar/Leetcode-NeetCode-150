class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        cntS, cntT = {},{}

        for i in range(len(s)):
            cntS[s[i]] = 1 + cntS.get(s[i],0)
            cntT[t[i]] = 1 + cntT.get(t[i],0)

        #iterate over the maps and check for same count
        for c in cntS:
            if cntS[c] != cntT.get(c,0):
                return False

        return True
        
