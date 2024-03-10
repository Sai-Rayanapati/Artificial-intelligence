from pyamaze import maze, agent, COLOR, textLabel
import time
from queue import PriorityQueue


def manhattan_distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))


# heuristic
def h_score(cell1, cell2):
    return manhattan_distance(cell1, cell2)


def a_star(maze):
    start_cell = (maze.rows, maze.cols)
    goal_cell = (1,1)

    g_score = {cell: float('inf') for cell in maze.grid}
    f_score = {cell: float('inf') for cell in maze.grid}

    g_score[start_cell] = 0
    # f = g + h
    f_score[start_cell] = g_score[start_cell] + h_score(start_cell,goal_cell)

    open_cells = PriorityQueue()

    open_cells.put((h_score(start_cell, goal_cell), h_score(start_cell, goal_cell), start_cell))

    explored_path ={}
    explored_cells = []

    while not open_cells.empty():
        current_cell = open_cells.get()[2]

        if current_cell not in explored_cells:
            explored_cells.append(current_cell)

        if current_cell == goal_cell:
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

                updated_g_score = g_score[current_cell]+1
                updated_f_score = updated_g_score + h_score(child_cell,goal_cell)

                if updated_f_score < f_score[child_cell]:
                    g_score[child_cell] = updated_g_score
                    f_score[child_cell] = updated_f_score
                    open_cells.put((f_score[child_cell], h_score(child_cell, goal_cell), child_cell))
                    explored_path[child_cell] = current_cell

    a_star_path = {}
    cell = goal_cell

    while cell!=start_cell:
        a_star_path[explored_path[cell]] = cell
        cell = explored_path[cell]

    return a_star_path,explored_cells

if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze(loopPercent=50)

    a_star_path, explored_path = a_star(m)

    a = agent(m, footprints=True, filled=False)
    b = agent(m, footprints=True, color=COLOR.green)
    m.tracePath({b: explored_path}, delay=100)
    m.tracePath({a: a_star_path}, delay=100)

    m.run()


