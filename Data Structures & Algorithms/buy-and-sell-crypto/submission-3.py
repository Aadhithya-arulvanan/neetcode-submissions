class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = prices[0]
        pro = 0 
        for i in prices:
            lp = min(lp,i)
            pro = max (pro,i-lp)
        return pro