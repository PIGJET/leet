class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        
        projects = sorted(zip(capital, profits))
        heap = []
        n = len(projects)

        i = 0

        for project in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            
            if len(heap) == 0:
                return w 
            
            w -= heapq.heappop(heap)

        return w 
