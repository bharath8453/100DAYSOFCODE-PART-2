class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        # Use a large number instead of infinity
        MAX_DIST = 1000000
        
        # Initialize distance matrix
        dist = [[MAX_DIST] * n for _ in range(n)]
        
        # Distance to self is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Fill the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w  # because the graph is bidirectional
        
        # Floyd-Warshall algorithm to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities
        min_count = n
        result_city = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            # Choose city with smaller count, if tie, larger index
            if count <= min_count:
                min_count = count
                result_city = i
        
        return result_city

sol = Solution()
print(sol.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))  
print(sol.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))