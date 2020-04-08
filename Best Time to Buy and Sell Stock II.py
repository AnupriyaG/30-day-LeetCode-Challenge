class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =0
        total_profit=[]
        buying = True
        for i in range(0,len(prices)):
            if(buying):
                if(i != len(prices)-1 and prices[i]<prices[i+1]):
                    buy = prices[i]
                    buying = not buying
                else:
                    continue
            else:
                if(i != len(prices)-1 and prices[i]<prices[i+1]):
                    continue
                else:
                    total_profit.append(prices[i] - buy)
                    buying = not buying
        return sum(total_profit)