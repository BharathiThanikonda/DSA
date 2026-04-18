class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_s =defaultdict(int)
        for i in s:
            dict_s[i]+=1
        for j in t:
            if dict_s[j]!=t.count(j):
                return False
            
        return True
        