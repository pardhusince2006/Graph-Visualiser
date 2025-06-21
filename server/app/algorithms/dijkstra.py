from collections import defaultdict
import heapq

def dijkstra(nodes, edges, start, goal=None):
    # Create adjacency list with weights (default weight = 1)
    graph = defaultdict(list)
    for edge in edges:
        weight = edge.get('weight', 1)
        from_node = edge['from']
        to_node = edge['to']
        graph[from_node].append((to_node, weight))
        # For undirected graph, add reverse edge
        graph[to_node].append((from_node, weight))

    # Initialize distances
    distances = {node: float('infinity') for node in nodes}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = []
    previous = {}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue
            
        visited.append(current_node)
        
        # If we have a goal and we've reached it, we can stop
        if goal is not None and current_node == goal:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct all shortest paths from start
    all_paths = {}
    for node in nodes:
        if distances[node] == float('infinity'):
            all_paths[node] = {'path': [], 'cost': float('infinity')}
        else:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = previous.get(current)
            path.reverse()
            all_paths[node] = {'path': path, 'cost': distances[node]}
    
    # Reconstruct specific path if goal is specified
    path = None
    total_cost = None
    if goal is not None:
        if distances[goal] == float('infinity'):
            path = []
            total_cost = float('infinity')
        else:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = previous.get(current)
            path.reverse()
            total_cost = distances[goal]
    
    return {
        'visitedOrder': visited,
        'distances': distances,
        'previous': previous,
        'path': path,
        'totalCost': total_cost,
        'allPaths': all_paths
    } 