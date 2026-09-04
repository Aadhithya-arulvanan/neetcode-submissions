class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0  
        seen =set()
        h = 0
        while r < len(s):
            while r < len(s) and s[r] not in seen :    
                seen.add(s[r])
                r += 1
            h = max(h,r - l)
            if r >= len(s)   :
                return h
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
        return h    
            
