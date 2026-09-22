#Fast version 

#Slow version 
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[]
        for i in range(len(temperatures)):
            A = len(ans)
            for j in range(i+1, len(temperatures)):
                flag = False
                if temperatures[i] < temperatures[j]:
                    ans.append(j-i)
                    flag = True
                if flag:
                    break
            if A == len(ans):
                ans.append(0)
        return ans
