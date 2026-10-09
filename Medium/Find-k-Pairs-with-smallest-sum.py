# THis code tried to teach me heap

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        ans=[]
        h=[]
        i =1
        heapq.heappush(h,(nums1[0]+nums2[0],0,0))
        seen = set()
        while (len(ans)!=k):
            tup = heapq.heappop(h)
            if (tup[1], tup[2]) in seen:
                continue
            seen.add((tup[1], tup[2]))
            ans.append([nums1[tup[1]], nums2[tup[2]]])
            if (len(nums1)>tup[1] + 1):
                heapq.heappush(h,(nums1[tup[1]+1]+nums2[tup[2]],tup[1]+1,tup[2]))
            if (len(nums2)>tup[2] + 1):
                heapq.heappush(h,(nums1[tup[1]]+nums2[tup[2]+1],tup[1],tup[2]+1))
        return ans
