# Community-Detection-Modularity

Eigenvector-based community detection is a method used to identify communities or groups within a network by analyzing the eigenvectors of the network's adjacency matrix. The basic idea behind this approach is that nodes that belong to the same community will be more strongly connected to each other than to nodes in other communities.

The method starts by calculating the adjacency matrix of the network, which represents the connections between nodes. Next, the eigenvalues and eigenvectors of this matrix are calculated. The eigenvectors with the largest eigenvalues are then used to assign nodes to communities.

The basic idea is that nodes that belong to the same community will have similar eigenvector values for these dominant eigenvectors. By grouping nodes with similar eigenvector values together, communities can be identified.

The method starts by calculating the adjacency matrix of the network, which represents the connections between nodes. Next, the eigenvalues and eigenvectors of this matrix are calculated. The eigenvectors with the largest eigenvalues are then used to assign nodes to communities.

The basic idea is that nodes that belong to the same community will have similar eigenvector values for these dominant eigenvectors. By grouping nodes with similar eigenvector values together, communities can be identified.

## Installation

### Install via PIP
```cmd
pip install apache-age-community-detection
```

### Build from Source
```cmd
sudo apt-get update
sudo apt-get install libeigen3-dev
git clone https://github.com/Munmud/Community-Detection-Modularity
cd Community-Detection-Modularity
python setup.py install
```

### Unit Test
```cmd
python -m unittest test_community.py
```

## Instruction

### import
```py
from age_cda import Graph
```

### Create Graph
```py
nodes = [0, 1, 2, 3, 4, 5]
edges = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5]]
g = Graph.Graph()
g.createGraph(nodes, edges)
```
- Nodes : `any`
- Edges : 
    - `2d array : adjacency list`
    - `Each element within Nodes array

### Generate Community Assignment
```py
res = g.get_community()
```

### Output Format
```
[[3,4,5],[0,1,2]]
```
- List community
- Each community has list of nodes

### Samples
- [Creating Graph](https://github.com/Munmud/Community-Detection-Modularity/blob/main/Samples/sample1.py)
- [Zachary's karate club](https://github.com/Munmud/Community-Detection-Modularity/blob/main/Samples/sample2.py)

### Reference
- [Finding community structure in networks using the eigenvectors of matrices](https://arxiv.org/pdf/physics/0605087.pdf)
- [Modularity and community structure in networks](https://www.pnas.org/doi/10.1073/pnas.0601602103)
- [Statistical Mechanics of Community Detection](https://ia903002.us.archive.org/33/items/arxiv-cond-mat0603718/cond-mat0603718.pdf)
