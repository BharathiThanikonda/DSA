class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        best_buy =prices[0]
        p=0
        for i in prices:
            p=max(p,i-best_buy)
            best_buy = min(best_buy,i)
        return p

       


        