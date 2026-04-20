class Solution:
    def isValid(self, s: str) -> bool:
        d={'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if i in d.values():
                stack.append(i)
            if i in d.keys():
                if stack and d[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False


        