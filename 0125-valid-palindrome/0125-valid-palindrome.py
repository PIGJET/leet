class Solution(object):
    def isPalindrome(self, s):
        ans = ""


        for i in s:
            if i.isalnum():
                ans += i
        
        if len(ans) ==0:
            return True
        left = 0 
        right = len(ans) - 1
        ans = ans.lower()

        while left < right:
            if ans[left] != ans[right]:
                return False
            else:
                left += 1
                right -= 1
        return True 


