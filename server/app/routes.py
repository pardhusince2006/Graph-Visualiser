from flask import Blueprint, request, jsonify
from .algorithms.bfs import bfs
from .algorithms.dfs import dfs
from .algorithms.dijkstra import dijkstra
from .algorithms.toposort import topological_sort

api = Blueprint("api", __name__)

@api.route('/api/bfs', methods=['POST'])
def handle_bfs():
    data = request.get_json()
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])
    start = data.get('start', 0)
    result = bfs(nodes, edges, start)
    return jsonify(result)

@api.route('/api/dfs', methods=['POST'])
def handle_dfs():
    data = request.get_json()
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])
    start = data.get('start', 0)
    result = dfs(nodes, edges, start)
    return jsonify(result)

@api.route('/api/dijkstra', methods=['POST'])
def handle_dijkstra():
    data = request.get_json()
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])
    start = data.get('start', 0)
    goal = data.get('goal', None)
    result = dijkstra(nodes, edges, start, goal)
    return jsonify(result)

@api.route('/api/toposort', methods=['POST'])
def handle_toposort():
    data = request.get_json()
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])
    result = topological_sort(nodes, edges)
    return jsonify(result)

@api.route('/api/algorithms', methods=['GET'])
def get_algorithms():
    algorithms = [
        {'name': 'BFS', 'description': 'Breadth-First Search', 'endpoint': '/api/bfs'},
        {'name': 'DFS', 'description': 'Depth-First Search', 'endpoint': '/api/dfs'},
        {'name': 'Dijkstra', 'description': 'Shortest Path Algorithm', 'endpoint': '/api/dijkstra'},
        {'name': 'Topological Sort', 'description': 'Topological Sort for DAGs', 'endpoint': '/api/toposort'}
    ]
    return jsonify(algorithms)
