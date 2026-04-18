class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        freq=[[] for _ in range(len(nums)+1)]
        res=[]
        for i in nums:
            d[i]+=1
        for i,j in d.items():
            freq[j].append(i)
        for j in range(len(freq)-1,0,-1):
            for i in freq[j]:
                res.append(i)
                if k==len(res):
                    return res

        