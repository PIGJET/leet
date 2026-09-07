class Solution(object):
    def numRescueBoats(self, people, limit):
        ordered = sorted(people)
        left = 0 
        right = len(people) -1 
        ans = 0


        while left <= right:
            if ordered[left] + ordered[right] <= limit:
                left += 1

            right -= 1
            ans += 1

        return ans

