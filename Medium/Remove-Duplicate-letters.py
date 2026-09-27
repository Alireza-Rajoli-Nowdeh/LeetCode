# in this problem I learn how to use Dictionary, how loop over an string using enumerate(), how use set() (add() / remove()) and ...
#This problem is perfect in understanding set(),List[],Dictionary{}
# we can compare letters in alphabet!!!!!
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        result= []
        last = {}
        for i , char in enumerate(s):
            last[char] = i
        for i,char in enumerate(s):
            if char in seen:
                continue
            while len(result)>0 and result[-1] > char  and last[result[-1]] > i:
                 popped = result.pop()
                 seen.remove(popped)
            result.append(char)
            seen.add(char)
        return "".join(result)
