class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i, num in enumerate(nums):
            composite = target - num 

            if composite in hash:
                return (hash[composite], i)
            
            hash[num] = i 