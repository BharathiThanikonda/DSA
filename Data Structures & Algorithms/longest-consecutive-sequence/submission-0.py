class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest=0
        for i in nums:
            curr=i
            l=1
            while curr+1 in store:
                l+=1
                curr+=1
            longest= max(longest,l)
        return longest
        