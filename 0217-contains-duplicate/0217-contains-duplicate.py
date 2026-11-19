class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for i in nums: 
            seen.add(i)

        return len(nums) != len(seen)
