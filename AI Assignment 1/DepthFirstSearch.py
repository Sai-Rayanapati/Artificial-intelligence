from pyamaze import maze, agent, COLOR
import time


def dfs(maze):
    explored_cells = []
    cells_to_explore = [(maze.rows, maze.cols)]
    explored_paths = {}

    #For first iteration
    explored_cells.append((maze.rows, maze.cols))

    while len(cells_to_explore) > 0:
        current_cell = cells_to_explore.pop()

        # Goal reached condition
        if current_cell == (1, 1):
            break

        for open_direction in 'ESNW':
            if maze.maze_map[current_cell][open_direction]:
                if open_direction == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif open_direction == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif open_direction == 'S':
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif open_direction == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])

                if child_cell in explored_cells:
                    continue

                explored_cells.append(child_cell)
                cells_to_explore.append(child_cell)
                explored_paths[child_cell] = current_cell

    dfs_path = {}
    cell = (1, 1)
    while cell != (maze.rows, maze.cols):
        dfs_path[explored_paths[cell]] = cell
        cell = explored_paths[cell]
    return dfs_path, explored_cells


if __name__ == '__main__':
    m = maze(10,10)
    m.CreateMaze(loopPercent=50)
    start_time = time.time()
    dfs_path, explored_cells_path = dfs(m)
    end_time = time.time()
    total_time_taken = end_time-start_time
    print(total_time_taken)
    no_explored = len(explored_cells_path)
    total_cells = m.rows*m.cols
    cells_in_dfs_path = len(dfs_path)
    print(no_explored)
    print(total_cells)
    print(cells_in_dfs_path)
    a = agent(m, footprints=True, filled=False)
    b = agent(m, footprints=True, color=COLOR.green)
    m.tracePath({b: explored_cells_path}, delay=100)
    m.tracePath({a: dfs_path}, delay=100)

    m.run()
