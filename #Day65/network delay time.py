class Solution(object):
    def networkDelayTime(self, times, n, k):
        # Build adjacency list
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        # Initialize distances with infinity
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        
        visited = set()
        
        for _ in range(n):
            # Pick the unvisited node with the smallest distance
            min_node = None
            min_dist = float('inf')
            for node in range(1, n+1):
                if node not in visited and dist[node] < min_dist:
                    min_dist = dist[node]
                    min_node = node
            
            if min_node is None:
                break  # Remaining nodes are unreachable
            
            visited.add(min_node)
            
            # Update distances for neighbors
            if min_node in graph:
                for neighbor, wt in graph[min_node]:
                    if neighbor not in visited:
                        dist[neighbor] = min(dist[neighbor], dist[min_node] + wt)
        
        # If any node is still at infinity, it is unreachable
        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1

sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(sol.networkDelayTime([[1,2,1]], 2, 1))              
print(sol.networkDelayTime([[1,2,1]], 2, 2))   