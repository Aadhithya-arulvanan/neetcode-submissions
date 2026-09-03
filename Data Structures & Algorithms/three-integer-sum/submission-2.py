class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = set()
        for i in range(len(nums)-1):
            
            left = i+1 
            right = len(nums)-1
            while left < right :
                tot = s[left]+ s[right]+ s[i]
                if tot == 0:
                    res.add(tuple([s[left],s[right],s[i]]))
                    left +=1
                    right -=1
                elif tot < 0:
                    left +=1
                else :
                    right -=1
        return (list(res))