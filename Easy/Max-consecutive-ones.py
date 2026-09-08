# This problem teaches how you can use = and ++ and what's their difference. Also teaches how we can use len (...)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MC = 0
        Max = 0
        n = len(nums) 
        for i in range(n):
            if nums[i]==1:
                MC = MC + 1
                if MC > Max:
                    Max= MC
            if nums[i]==0:
                MC=0
        return Max
