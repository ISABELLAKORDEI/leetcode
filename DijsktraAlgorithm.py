# Just for Fun... thought about this algorithm and is actually used in network routing so plus
import heapq

def dijsktra(graph, start_node):
    visited_nodes =set()
    distances = {start_node: 0}
    priority_queue =[(0, start_node)]

    while priority_queue:
        (node, weight)  = heapq.heappop(priority_queue)

        if node not in visited_nodes:
            visited_nodes.add(node)
            for neighbor, distance in graph[node].items():
                if neighbor not in distances or distances[node] + distance < distances[neighbor]:
                    distances[neighbor] = distances[node] + distance 
                    
                    #adding the neighbour to the priority queue
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

        return distances

