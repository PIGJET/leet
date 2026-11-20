class Solution(object):
    def topKFrequent(self, nums, k):
        ans = defaultdict(int)
        
        for i in nums: 
            ans[i] += 1

        most = sorted(ans, key=ans.get, reverse = True)
        
        return most[:k]
