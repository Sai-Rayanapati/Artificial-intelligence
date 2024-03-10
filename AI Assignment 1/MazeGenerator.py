from pyamaze import maze


def generate_maze(x,y, loopPercent, pattern):
    m = maze(x, y)
    m.CreateMaze(loopPercent=loopPercent,pattern=pattern)
    return m

if __name__ == '__main__':
    maze = generate_maze(5,5,50,"none")
    print(maze.maze_map)

