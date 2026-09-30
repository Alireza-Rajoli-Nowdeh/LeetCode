#in Python number 0 consider as false / this question isabout using queues
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        Z = 0
        while tickets[k]:
            P = tickets.pop(0)
            P =P-1
            Z = Z+1
            if P !=0:
                tickets.append(P)
            if P ==0 and k==0:
                break
            if k ==0:
                k = len(tickets)-1
            else:
                k = k-1
        return Z

        
