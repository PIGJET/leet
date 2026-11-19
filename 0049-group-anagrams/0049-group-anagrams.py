class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            ans[key].append(i)

        return ans.values()