from collections import defaultdict
import heapq

class Graph():
    def __init__(self):
        self.edges = defaultdict(dict)
    
    def add_edge(self, from_node, to_node, weight):
        if to_node in self.edges[from_node].keys():
            if self.edges[from_node][to_node] > weight:
                self.edges[from_node][to_node] = weight
                self.edges[to_node][from_node] = weight
        else:
            self.edges[from_node][to_node] = weight
            self.edges[to_node][from_node] = weight
    
    def dijkstra(self, start):
        min_heap = []
        dist = { v: float('inf') for v in self.edges.keys() }

        heapq.heappush(min_heap, (0, start))
        dist[start] = 0

        while min_heap:
            current_dist, current_v = heapq.heappop(min_heap)
            
            for next_v, next_dist in self.edges[current_v].items():
                total_dist = current_dist + next_dist
                
                if total_dist < dist[next_v]:
                    dist[next_v] = total_dist
                    heapq.heappush(min_heap, (total_dist, next_v))
        
        return dist

def solution(N, road, K):
    answer = 0
    g = Graph()
    
    for arr in road:
        g.add_edge(arr[0], arr[1], arr[2])
    
    dist = g.dijkstra(1)
    for key in dist.keys():
        if dist[key] <= K:
            answer += 1
    return answer