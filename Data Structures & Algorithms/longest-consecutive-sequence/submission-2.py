class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest=0
        for i in nums:
            l=1
            if i-1 not in store:
                
                curr=i
                
                while curr+1 in store:
                    l+=1
                    curr+=1
            longest= max(longest,l)
        return longest
        