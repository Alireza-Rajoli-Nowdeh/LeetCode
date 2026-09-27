#The idea was same as temperature but more advance because it should somhow find the width of rectangle / there is good thrick that appendign 0 in order to avoid missing last element in list 
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while len(stack)>0 and heights[i]< heights[stack[-1]]:
                popped = stack.pop()
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1]-1
                area = heights[popped]*width
                if area > ans:
                    ans = area
            stack.append(i)
        return ans


        
