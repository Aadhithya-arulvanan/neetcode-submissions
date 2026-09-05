class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 ={}
        f2 ={}
        for i in s1:
            f1[i] = f1.get(i,0)+1
        l = 0
        for r in range(len(s2)):
            f2[s2[r]] = f2.get(s2[r],0)+1
            while f2[s2[r]]>f1.get(s2[r],0):
                f2[s2[l]] = f2.get(s2[l],0)-1
                l += 1 
            if r-l+1 == len(s1):
                return True 
        return False