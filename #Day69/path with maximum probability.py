class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))

        # Custom heap functions (max heap)
        def heappush(heap, item):
            heap.append(item)
            i = len(heap) - 1
            while i > 0:
                parent = (i - 1) // 2
                if heap[parent][0] >= heap[i][0]:
                    break
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent

        def heappop(heap):
            if not heap:
                return None
            root = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < len(heap) and heap[left][0] > heap[largest][0]:
                    largest = left
                if right < len(heap) and heap[right][0] > heap[largest][0]:
                    largest = right
                if largest == i:
                    break
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
            return root

        # Dijkstra-like algorithm (using max heap)
        prob = [0.0] * n
        prob[start_node] = 1.0
        heap = []
        heappush(heap, (1.0, start_node))

        while heap:
            curr_prob, node = heappop(heap)
            if node == end_node:
                return curr_prob
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heappush(heap, (new_prob, neighbor))

        return 0.0

s = Solution()
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)) 
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))  
print(s.maxProbability(3, [[0,1]], [0.5], 0, 2))                    
