class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Use a very large number to represent "infinity"
        MAX = 10**9
        
        # Initialize distances: set all to MAX except the source
        dist = [MAX] * n
        dist[src] = 0
        
        # Run modified Bellman-Ford for at most k+1 edges
        for _ in range(k + 1):
            temp = dist[:]  # Copy of previous distances
            for u, v, w in flights:
                if dist[u] != MAX:
                    if temp[v] > dist[u] + w:
                        temp[v] = dist[u] + w
            dist = temp
        
        # If destination is still MAX, return -1
        if dist[dst] == MAX:
            return -1
        else:
            return dist[dst]

sol = Solution()
print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)) 
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))                  
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))                
