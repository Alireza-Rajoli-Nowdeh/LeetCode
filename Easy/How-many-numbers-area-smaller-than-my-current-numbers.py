#Slow appraoch
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        List = []
        K = 0
        for i in range(len(nums)):
            for j in range (len(nums)):
                if nums[i] > nums[j]:
                    K = K +1
            List.append(K)
            K=0
        return List

  #Fast
  # Using Dictionary makes it super fast because it doesn't have scanning / Using Sorted() for sorting elements of a list / using not in for dictionaries / using enumerate

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        d = {}
        sortnums = sorted(nums)
        for index, value in enumerate(sortnums):
            if value not in d:
                d[value] = index
        for i in nums:
            ans.append(d[i])
        return ans
