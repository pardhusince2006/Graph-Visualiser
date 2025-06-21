# Graph Visualizer

A modern web application for visualizing graph algorithms with an interactive interface. Built with React frontend and Flask backend.

## Features

- **Interactive Graph Construction**: Build custom graphs with nodes and weighted edges
- **Multiple Algorithms**: 
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra's Shortest Path
  - Topological Sort
- **Real-time Visualization**: Watch algorithms execute step-by-step with color-coded nodes and edges
- **Modern UI**: Beautiful glass morphism design with smooth animations
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

### Backend
- **Python 3.12**
- **Flask**: Web framework
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **React 18**: UI library
- **D3.js**: Graph visualization
- **CSS3**: Modern styling with gradients and animations

## Project Structure

```
graph-visualizer/
├── client/                 # React frontend
│   ├── public/
│   │   ├── components/
│   │   │   ├── AlgorithmSelector.js
│   │   │   ├── GraphConstructor.js
│   │   │   └── GraphVisualizer.js
│   │   └── App.js
│   └── package.json
├── server/                 # Flask backend
│   ├── app/
│   │   ├── algorithms/
│   │   │   ├── bfs.py
│   │   │   ├── dfs.py
│   │   │   ├── dijkstra.py
│   │   │   └── toposort.py
│   │   └── routes.py
│   └── run.py
└── README.md
```

## Installation

### Prerequisites
- Python 3.12+
- Node.js 16+
- npm

### Backend Setup

1. Navigate to the project directory:
   ```bash
   cd graph-visualizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install flask flask-cors
   ```

4. Start the Flask server:
   ```bash
   python server/run.py
   ```
   The backend will run on `http://127.0.0.1:5001`

### Frontend Setup

1. Navigate to the client directory:
   ```bash
   cd client
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   The frontend will run on `http://localhost:3000`

## Usage

1. **Build a Graph**: Use the graph constructor to add nodes and edges
2. **Select Algorithm**: Choose from BFS, DFS, Dijkstra, or Topological Sort
3. **Configure Parameters**: Set start node, goal node (for Dijkstra), or other algorithm-specific parameters
4. **Run Visualization**: Watch the algorithm execute with step-by-step visualization
5. **Control Playback**: Use play, pause, next, and previous controls

## API Endpoints

- `GET /api/algorithms` - Get available algorithms
- `POST /api/bfs` - Run Breadth-First Search
- `POST /api/dfs` - Run Depth-First Search
- `POST /api/dijkstra` - Run Dijkstra's algorithm
- `POST /api/toposort` - Run Topological Sort

## Algorithm Details

### BFS (Breadth-First Search)
- Explores all neighbors at the current depth before moving to the next level
- Useful for finding shortest paths in unweighted graphs
- Time Complexity: O(V + E)

### DFS (Depth-First Search)
- Explores as far as possible along each branch before backtracking
- Useful for topological sorting and cycle detection
- Time Complexity: O(V + E)

### Dijkstra's Algorithm
- Finds shortest paths from a source node to all other nodes
- Works with weighted graphs (positive weights only)
- Time Complexity: O((V + E) log V)

### Topological Sort
- Orders nodes in a directed acyclic graph (DAG)
- Useful for dependency resolution and scheduling
- Time Complexity: O(V + E)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- D3.js for graph visualization capabilities
- React community for excellent documentation and tools
- Flask for the robust backend framework 