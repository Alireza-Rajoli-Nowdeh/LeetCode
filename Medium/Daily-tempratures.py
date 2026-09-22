#Fast version/ Top of stack is stack[-1]/ using while() for popping untill condition stasfied
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i]> temperatures[stack[-1]]:
                popped = stack.pop()
                ans[popped] = i - popped
            stack.append(i)

        return ans

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
