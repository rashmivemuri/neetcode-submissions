class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        buy=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-buy
            if profit>0 and profit>max:
                max=profit
            buy=min(buy,prices[i])

        
        return max
                
            
            
        