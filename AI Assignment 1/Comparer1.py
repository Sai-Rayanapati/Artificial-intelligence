import os
import psutil
from MazeGenerator import generate_maze
from BreadthFirstSearch import bfs
from DepthFirstSearch import dfs
from A_Star import a_star
import time
import pandas as pd
import gc


def memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Return memory usage in MB


maze_dimensions = [5, 10, 20, 50, 100]
loop_percent = [0, 50, 100]
patterns = ["none", 'v', 'h']
results = []

no_of_iterations = 10


for dimensions in maze_dimensions:
    bfs_metrics = [0, 0, 0, 0]  # path length, cells explored, time taken, memory used
    dfs_metrics = [0, 0, 0, 0]
    a_star_metrics = [0, 0, 0, 0]
    for iteration in range(no_of_iterations):
        maze = generate_maze(dimensions, dimensions, 50, "none")

        mem_before = memory_usage()
        bfs_start_time = time.perf_counter()
        bfs_path, bfs_explored_cells_path = bfs(maze)
        bfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        bfs_metrics[0] += len(bfs_path)+1
        bfs_metrics[1] += len(bfs_explored_cells_path)
        bfs_metrics[2] += (bfs_end_time - bfs_start_time)
        bfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        dfs_start_time = time.perf_counter()
        dfs_path, dfs_explored_cells_path = dfs(maze)
        dfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        dfs_metrics[0] += len(dfs_path)+1
        dfs_metrics[1] += len(dfs_explored_cells_path)
        dfs_metrics[2] += (dfs_end_time - dfs_start_time)
        dfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        a_star_start_time = time.perf_counter()
        a_star_path, a_star_explored_cells_path = a_star(maze)
        a_star_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        a_star_metrics[0] += len(a_star_path)+1
        a_star_metrics[1] += len(a_star_explored_cells_path)
        a_star_metrics[2] += (a_star_end_time - a_star_start_time)
        a_star_metrics[3] += (mem_after - mem_before)

    # Calculate averages
    bfs_avg = [x / no_of_iterations for x in bfs_metrics]
    dfs_avg = [x / no_of_iterations for x in dfs_metrics]
    a_star_avg = [x / no_of_iterations for x in a_star_metrics]

    # Append the results for each algorithm
    results.append(['BFS', dimensions] + bfs_avg)
    results.append(['DFS', dimensions] + dfs_avg)
    results.append(['A*', dimensions] + a_star_avg)

# Create a DataFrame
df = pd.DataFrame(results,
                  columns=['Algorithm', 'Dimensions', 'Shortest Path Length', 'No of Cells Explored', 'Time Taken (s)',
                           'Memory Usage (MB)'])

df.to_csv("Compare1_Dimensions.csv", index=False)

# Display the table
print(df)

results = []

for loop in loop_percent:
    bfs_metrics = [0, 0, 0, 0]  # path length, cells explored, time taken, memory used
    dfs_metrics = [0, 0, 0, 0]
    a_star_metrics = [0, 0, 0, 0]

    for iteration in range(no_of_iterations):
        maze = generate_maze(100, 100, loop, "none")

        mem_before = memory_usage()
        bfs_start_time = time.perf_counter()
        bfs_path, bfs_explored_cells_path = bfs(maze)
        bfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        bfs_metrics[0] += len(bfs_path)+1
        bfs_metrics[1] += len(bfs_explored_cells_path)
        bfs_metrics[2] += (bfs_end_time - bfs_start_time)
        bfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        dfs_start_time = time.perf_counter()
        dfs_path, dfs_explored_cells_path = dfs(maze)
        dfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        dfs_metrics[0] += len(dfs_path)+1
        dfs_metrics[1] += len(dfs_explored_cells_path)
        dfs_metrics[2] += (dfs_end_time - dfs_start_time)
        dfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        a_star_start_time = time.perf_counter()
        a_star_path, a_star_explored_cells_path = a_star(maze)
        a_star_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        a_star_metrics[0] += len(a_star_path)+1
        a_star_metrics[1] += len(a_star_explored_cells_path)
        a_star_metrics[2] += (a_star_end_time - a_star_start_time)
        a_star_metrics[3] += (mem_after - mem_before)


    # Calculate averages
    bfs_avg = [x / no_of_iterations for x in bfs_metrics]
    dfs_avg = [x / no_of_iterations for x in dfs_metrics]
    a_star_avg = [x / no_of_iterations for x in a_star_metrics]

    # Append the results for each algorithm
    results.append(['BFS', loop] + bfs_avg)
    results.append(['DFS', loop] + dfs_avg)
    results.append(['A*', loop] + a_star_avg)

# Create a DataFrame
df = pd.DataFrame(results,
                  columns=['Algorithm', 'Loop Percent(%)', 'Shortest Path Length', 'No of Cells Explored', 'Time Taken (s)',
                           'Memory Usage (MB)'])

df.to_csv("Compare1_loops.csv", index=False)

# Display the table
print(df)

results = []


for pattern in patterns:
    bfs_metrics = [0, 0, 0, 0]  # path length, cells explored, time taken, memory used
    dfs_metrics = [0, 0, 0, 0]
    a_star_metrics = [0, 0, 0, 0]

    for iteration in range(no_of_iterations):
        maze = generate_maze(100, 100, 50, pattern)

        mem_before = memory_usage()
        bfs_start_time = time.perf_counter()
        bfs_path, bfs_explored_cells_path = bfs(maze)
        bfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        bfs_metrics[0] += len(bfs_path)+1
        bfs_metrics[1] += len(bfs_explored_cells_path)
        bfs_metrics[2] += (bfs_end_time - bfs_start_time)
        bfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        dfs_start_time = time.perf_counter()
        dfs_path, dfs_explored_cells_path = dfs(maze)
        dfs_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        dfs_metrics[0] += len(dfs_path)+1
        dfs_metrics[1] += len(dfs_explored_cells_path)
        dfs_metrics[2] += (dfs_end_time - dfs_start_time)
        dfs_metrics[3] += (mem_after - mem_before)

        mem_before = memory_usage()
        a_star_start_time = time.perf_counter()
        a_star_path, a_star_explored_cells_path = a_star(maze)
        a_star_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        a_star_metrics[0] += len(a_star_path)+1
        a_star_metrics[1] += len(a_star_explored_cells_path)
        a_star_metrics[2] += (a_star_end_time - a_star_start_time)
        a_star_metrics[3] += (mem_after - mem_before)

    # Calculate averages
    bfs_avg = [x / no_of_iterations for x in bfs_metrics]
    dfs_avg = [x / no_of_iterations for x in dfs_metrics]
    a_star_avg = [x / no_of_iterations for x in a_star_metrics]

    # Append the results for each algorithm
    results.append(['BFS', pattern] + bfs_avg)
    results.append(['DFS', pattern] + dfs_avg)
    results.append(['A*', pattern] + a_star_avg)

# Create a DataFrame
df = pd.DataFrame(results,
                  columns=['Algorithm', 'Pattern', 'Shortest Path Length', 'No of Cells Explored', 'Time Taken (s)',
                           'Memory Usage (MB)'])

df.to_csv("Compare1_pattern.csv", index=False)

# Display the table
print(df)

