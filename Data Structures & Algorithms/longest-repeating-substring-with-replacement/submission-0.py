class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = l = 0
        frq = {}
        m = 0
        for r in range(len(s)):
            frq[s[r]] = frq.get(s[r],0)+1
             
            while r-l+1 > max(frq.values())+ k:
                frq[s[l]] = frq.get(s[l],0)-1
                l += 1 
            m = max(m,r-l+1)
        return m
