from collections import defaultdict

def dfs(nodes, edges, start):
    # Create adjacency list for undirected graph
    graph = defaultdict(list)
    for edge in edges:
        from_node = edge['from']
        to_node = edge['to']
        graph[from_node].append(to_node)
        # For undirected graph, add reverse edge
        graph[to_node].append(from_node)

    visited = []
    seen = set()

    def dfs_recursive(node):
        if node in seen:
            return
        seen.add(node)
        visited.append(node)
        
        # Get all neighbors and sort them for consistent ordering
        neighbors = sorted(graph[node])
        for neighbor in neighbors:
            if neighbor not in seen:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return {'visitedOrder': visited} 