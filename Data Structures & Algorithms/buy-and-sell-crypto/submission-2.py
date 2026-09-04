class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hp = 0
        for i in range (len(prices)-1 ):
            for m in range(i+1 ,len(prices)):
                hp = max(hp,prices[m]-prices[i])
        return hp 