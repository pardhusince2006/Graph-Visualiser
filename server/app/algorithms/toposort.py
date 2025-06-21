from collections import defaultdict, deque

def topological_sort(nodes, edges):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    Returns a linear ordering of vertices where for every directed edge (u, v),
    vertex u comes before vertex v in the ordering.
    """
    if not nodes or not edges:
        return {
            'visitedOrder': [],
            'path': [],
            'totalCost': 0,
            'message': 'Empty graph'
        }
    
    # Create adjacency list for directed graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all nodes
    for node in nodes:
        in_degree[node] = 0
    
    # Build graph and calculate in-degrees
    for edge in edges:
        from_node = edge['from']
        to_node = edge['to']
        graph[from_node].append(to_node)
        in_degree[to_node] += 1
    
    # Find all nodes with in-degree 0 (no incoming edges)
    queue = deque([node for node in nodes if in_degree[node] == 0])
    visited = []
    result_order = []
    
    # Process nodes in topological order
    while queue:
        current = queue.popleft()
        visited.append(current)
        result_order.append(current)
        
        # Reduce in-degree of all neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if we have a valid topological sort
    if len(result_order) != len(nodes):
        return {
            'visitedOrder': visited,
            'path': [],
            'totalCost': 0,
            'message': 'Graph contains cycles - topological sort not possible'
        }
    
    return {
        'visitedOrder': visited,
        'path': result_order,
        'totalCost': len(result_order),
        'message': 'Valid topological sort found'
    } 