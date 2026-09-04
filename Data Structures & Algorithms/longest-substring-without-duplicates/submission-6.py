class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0  
        seen = {}
        h = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1,l)
            h = max(h,r-l+1)
            seen[s[r]] = r 
        return h    
            
