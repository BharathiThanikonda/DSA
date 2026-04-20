class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=0
        s1_c = defaultdict(int)
        s2_c=defaultdict(int)
        for i in s1:
            s1_c[i]+=1
        for i in range(len(s1)):
            s2_c[s2[i]]+=1
        if s1_c==s2_c:
            return True

        for r in range(len(s1),len(s2)):
            s2_c[s2[r]]+=1
            s2_c[s2[l]]-=1
            if s2_c[s2[l]]==0:
                del s2_c[s2[l]]
            l+=1
            if s1_c==s2_c:
                return True
            
        return False
