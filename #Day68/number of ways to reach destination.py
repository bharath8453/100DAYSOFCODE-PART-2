class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Initialize arrays
        dist = [10**15] * n   # very large number instead of inf
        ways = [0] * n
        visited = [False] * n

        dist[0] = 0
        ways[0] = 1

        for _ in range(n):
            # Find the unvisited node with smallest distance
            min_node = -1
            min_dist = 10**15
            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    min_node = i

            if min_node == -1:
                break

            visited[min_node] = True

            # Explore neighbors
            for nei, time in graph[min_node]:
                new_time = dist[min_node] + time

                # Found a shorter path
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[min_node]

                # Found another shortest path
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[min_node]) % MOD

        return ways[n - 1] % MOD

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],
          [2,5,1],[0,4,5],[4,6,2]]

print(Solution().countPaths(n, roads))