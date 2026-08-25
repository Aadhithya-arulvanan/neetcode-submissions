class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store =set(nums)
        j =0
        if not store :
            return 0
        for i in store:
            if i - 1 not in store :
                k = 1
                while i +k in store :
                    k +=1 
                j = max(j, k)
        return j ;    

                