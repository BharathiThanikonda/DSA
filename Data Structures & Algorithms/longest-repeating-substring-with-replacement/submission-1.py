class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        c=defaultdict(int)
        res=0
        for r in range(len(s)):
            c[s[r]]+=1

            
            if (r-l+1) - max(c.values())>k:
                c[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
               
            
                
            
            
        return res