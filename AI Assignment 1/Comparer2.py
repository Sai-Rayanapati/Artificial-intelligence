import os
import psutil
from MazeGenerator import generate_maze
from PolicyIteration import policyIteration
from ValueIteration import valueIteration
import time
import pandas as pd
import gc

def memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Return memory usage in MB


maze_dimensions = [5, 10, 20, 50, 100]
loop_percent = [100,50,0]
patterns = ["none", 'v', 'h']
results = []

no_of_iterations = 10

for dimensions in maze_dimensions:
    PI_metrics = [0, 0, 0]
    VI_metrics = [0, 0, 0]

    for iteration in range(no_of_iterations):
        maze = generate_maze(dimensions, dimensions, 50, "none")

        mem_before = memory_usage()
        PI_start_time = time.perf_counter()
        PI_path = policyIteration(maze)
        PI_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        PI_metrics[0] += len(PI_path)
        PI_metrics[1] += (PI_end_time - PI_start_time)
        PI_metrics[2] += mem_after - mem_before

        mem_before = memory_usage()
        VI_start_time = time.perf_counter()
        VI_path = valueIteration(maze)
        VI_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        VI_metrics[0] += len(VI_path)
        VI_metrics[1] += (VI_end_time - VI_start_time)
        VI_metrics[2] += mem_after - mem_before

    PI_avg = [x / no_of_iterations for x in PI_metrics]
    VI_avg = [x / no_of_iterations for x in VI_metrics]

    results.append(['Policy Iteration', dimensions] + PI_avg)
    results.append(['Value Iteration', dimensions] + VI_avg)

df = pd.DataFrame(results,
                  columns=['Algorithm', 'Dimensions', 'Shortest Path Length', 'Time Taken (s)', 'Memory Usage (MB)'])

df.to_csv("Compare2_Dimensions.csv", index=False)

print(df)

results = []

for loop in loop_percent:
    PI_metrics = [0, 0, 0]
    VI_metrics = [0, 0, 0]

    for iteration in range(no_of_iterations):
        maze = generate_maze(20, 20, loop, "none")

        mem_before = memory_usage()
        PI_start_time = time.perf_counter()
        PI_path = policyIteration(maze)
        PI_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        PI_metrics[0] += len(PI_path)
        PI_metrics[1] += (PI_end_time - PI_start_time)
        PI_metrics[2] += mem_after - mem_before

        if loop == 0:
            continue
        else:
            mem_before = memory_usage()
            VI_start_time = time.perf_counter()
            VI_path = valueIteration(maze)
            VI_end_time = time.perf_counter()
            gc.collect()
            mem_after = memory_usage()
            VI_metrics[0] += len(VI_path)
            VI_metrics[1] += (VI_end_time - VI_start_time)
            VI_metrics[2] += mem_after - mem_before

    PI_avg = [x / no_of_iterations for x in PI_metrics]
    VI_avg = [x / no_of_iterations for x in VI_metrics]

    results.append(['Policy Iteration', loop] + PI_avg)
    results.append(['Value Iteration', loop] + VI_avg)

df = pd.DataFrame(results,
                  columns=['Algorithm', 'Loop Percent (%)', 'Shortest Path Length', 'Time Taken (s)', 'Memory Usage (MB)'])

df.to_csv("Compare2_loops.csv", index=False)

print(df)

results = []

for pattern in patterns:
    PI_metrics = [0, 0, 0]
    VI_metrics = [0, 0, 0]

    for iteration in range(no_of_iterations):
        maze = generate_maze(20, 20, 50, pattern)

        mem_before = memory_usage()
        PI_start_time = time.perf_counter()
        PI_path = policyIteration(maze)
        PI_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        PI_metrics[0] += len(PI_path)
        PI_metrics[1] += (PI_end_time - PI_start_time)
        PI_metrics[2] += mem_after - mem_before

        mem_before = memory_usage()
        VI_start_time = time.perf_counter()
        VI_path = valueIteration(maze)
        VI_end_time = time.perf_counter()
        gc.collect()
        mem_after = memory_usage()
        VI_metrics[0] += len(VI_path)
        VI_metrics[1] += (VI_end_time - VI_start_time)
        VI_metrics[2] += mem_after - mem_before

    PI_avg = [x / no_of_iterations for x in PI_metrics]
    VI_avg = [x / no_of_iterations for x in VI_metrics]

    results.append(['Policy Iteration', pattern] + PI_avg)
    results.append(['Value Iteration', pattern] + VI_avg)

df = pd.DataFrame(results,
                  columns=['Algorithm', 'Pattern', 'Shortest Path Length', 'Time Taken (s)', 'Memory Usage (MB)'])

df.to_csv("Compare2_pattern.csv", index=False)

print(df)