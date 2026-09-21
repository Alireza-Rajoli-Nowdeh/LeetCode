#This question teaches how to use break
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = []
        for i in range(len(prices)):
            k=len(ans)
            for j in range (i+1, len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i]-prices[j])
                    break
            if len(ans) == k:
                ans.append(prices[i])
        return ans
            
