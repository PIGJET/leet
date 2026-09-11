class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) -1
        ans = [0] * len(nums)
        i = len(nums)-1


        while left <= right:
            if nums[left] ** 2 > nums[right] **2:
                ans[i] = nums[left] **2
                left +=1 
                 

            else:
                ans[i] = nums[right] ** 2
                right -= 1
                 
            i-=1

        return ans 
       
       