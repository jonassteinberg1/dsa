from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = set()
        hold = 0
        counter = 1

        while hold < len(prices):
            for price in range(len(prices)-1):
                if counter < len(prices) - 1:
                    if prices[counter] - prices[hold] > 0:
                        profits.add(prices[counter] - prices[hold])
                        counter += 1
                    else:
                        counter += 1
                        continue
            hold += 1
            counter = hold + 1
        
        return sorted(profits)[-1]
    
s = Solution()

s.maxProfit([1, 2, 3, 4, 0])


