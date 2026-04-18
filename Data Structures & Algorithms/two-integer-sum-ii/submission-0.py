class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            res = target-numbers[i]
            if res in d:
                return[d[res]+1,i+1]
            d[numbers[i]]=i


        