from collections import deque, defaultdict

def bfs(nodes, edges, start):
    # Create adjacency list for undirected graph
    graph = defaultdict(list)
    for edge in edges:
        from_node = edge['from']
        to_node = edge['to']
        graph[from_node].append(to_node)
        # For undirected graph, add reverse edge
        graph[to_node].append(from_node)

    visited = []
    queue = deque([start])
    seen = set([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        
        # Get all neighbors and sort them for consistent ordering
        neighbors = sorted(graph[node])
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return {'visitedOrder': visited}
