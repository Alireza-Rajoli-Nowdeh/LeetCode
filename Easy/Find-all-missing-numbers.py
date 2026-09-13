# finding numbers they are  missing a lits using set()
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        snums = set(nums)
        for i in range (1, len(nums)+1):
            if i not in snums:
                ans.append(i)
        return ans
