class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        c = 0
        for i in num:
            if i -1 not in num :
                k = 0 
                j = i
                while j in num :
                    j += 1 
                    k += 1
                if k > c :
                    c = k
            
        return c
