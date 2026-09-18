# This question letterally roasted me :). it had lots of thing to learn but mainly it's about how a call abck actually works and why stack is a natural solution for it.
# a, b, c = A.split("")/ [0]*n / is stack: / stack[][] were some new things I learned from this question
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0]*n
        stack = []
        for i in range(len(logs)):
            Id , action , time = logs[i].split(":")
            time = int(time)
            if action == "start" :
                if stack:
                    result[int(stack[-1][0])] += (time - stack[-1][1])
                stack.append([Id , time])
            else:
                top= stack.pop()
                result[int(top[0])] += time - top[1] +1 
                if stack:
                    stack[-1][1] = time + 1
        return result



        
