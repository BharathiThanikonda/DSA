class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        s1_c = defaultdict(int)
        for i in s1:
            s1_c[i]+=1

        for r in range(len(s1)-1,len(s2)):
            c=defaultdict(int)
            for i in s2[l:r+1]:
                c[i]+=1
            if s1_c.items()==c.items():
                return True
            l+=1
        return False
