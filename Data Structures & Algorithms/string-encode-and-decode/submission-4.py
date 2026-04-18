class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc+=str(len(i))+"#"+i
        return enc


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=i+1
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
        
