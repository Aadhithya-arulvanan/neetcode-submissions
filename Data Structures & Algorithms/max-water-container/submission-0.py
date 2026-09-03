class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        m = 0
        right = len(heights)-1
        while left < right:
            wl = min(heights[left],heights[right])
            space = wl * (right-left)
            m = max(m,space)
            if heights[left]<heights[right]:
                left +=1
            else :
                right -=1 
            

        return m 