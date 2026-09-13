# how can I use stack operation/ if we have a list there is two way to point last lement/ 1) target[-1]+1 & len(target)+1
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        for i in range(1,target[-1]+1):
            if i not in target:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
        return ans
