from collections import Counter


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse = True)

        while k:
            val = ordered[-1]

            if val <= k:
                k -= val 
                ordered.pop()

            else:
                break
            
        return len(ordered)