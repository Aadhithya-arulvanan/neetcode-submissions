class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = {}
        l = 0
        m=0
        for i in range(len(s)):
            k[s[i]]= k.get(s[i],0)+1
            while k[s[i]]>1:
                k[s[l]] = k.get(s[l],0)-1
                l +=1
            m = max(m,i-l+1) 
        return m