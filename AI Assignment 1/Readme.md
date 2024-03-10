# CS7IS2 Artificial Intelligence: Maze Solver

Below are the detailed instructions for installing and running various maze-solving algorithms, including Breadth First Search (BFS), Depth First Search (DFS), A*, Policy Iteration, and Value Iteration. These algorithms are implemented in Python and are designed to solve mazes efficiently.



## Prerequisites

- **Python Version**: Ensure you have Python 3.12.0 installed on your system.
- **Required Libraries**: The implementations rely on `pyamaze`, `numpy`, and `pandas` libraries.


### Installing
First, clone the repository to your local machine. Then, you need to install the necessary libraries. You can install all required dependencies by executing the following command in your terminal:

```sh
pip install -r requirements.txt
```

This command reads the requirements.txt file and installs the Python packages listed there.

### Running the Algorithms

Navigate to the cloned repository's directory in your terminal. From there, you can run the specific algorithm you're interested in testing.

### Search Algorithms


- **Breadth First Search (BFS):**
```sh
python BreadthFirstSearch.py
```

- **Depth First Search (DFS):**
```sh
python DepthFirstSearch.py
```

- **A* Search:** 
```sh
python A_Star.py
```

### Markov Decision Processes (MDP) Algorithms

- **Policy Iteration:**
```sh
python PolicyIteration.py
```

- **Value Iteration:**
```sh
python ValueIteration.py
```

#### Comparisons

To compare the performance of the algorithms, you can run one of the comparison scripts. These scripts generate tables that showcase the differences in performance among the algorithms.

- **Search Algorithms Comparison:**
```sh
python Comparer1.py
```

- **MDP Algorithms Comparison:**
```sh
python Comparer2.py
```

- **Search vs. MDP Algorithms Comparison:**
```sh
python Comparer3.py
```

