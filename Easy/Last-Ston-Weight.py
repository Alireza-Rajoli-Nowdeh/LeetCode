# This questions was trying to tach me Heap but unfortunately I used another appraoch :)
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            max1 = stones.pop()
            max2 = stones.pop()
            if max1-max2>0:
                stones.append(max1-max2)
        if stones == []:
            return 0
        else:
            return int(stones[0])



            
