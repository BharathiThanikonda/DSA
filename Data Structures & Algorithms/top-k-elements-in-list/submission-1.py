class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        
        for i in nums:
            d[i]+=1
        s=dict(sorted(d.items(),key=lambda x:x[1], reverse = True))
        print(s)
        l=list(s.keys())
        return l[:k]

        