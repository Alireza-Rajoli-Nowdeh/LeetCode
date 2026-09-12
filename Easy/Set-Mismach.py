#1)Slow approach

# using 2 for loops for checking candidate number and list elements/ range (start, stop) how it works/ using checkers after inner loops
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums)+1):
            K = 0
            for j in range(len(nums)):
                if i==nums[j]:
                    K = K+1
            if K == 2:
                ans.append(i)
            if K ==0:
                ans.append(i)
        return ans

#2) Fast appraoch

# Using "set ()" instead of scanning / Using "in" and "Not in" / Using "Sum()"

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        snums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in snums:
                missing = i
        duplicate = sum(nums)-sum(snums)
        return [duplicate, missing]
