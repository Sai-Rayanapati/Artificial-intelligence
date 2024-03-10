import numpy as np
from pyamaze import maze, agent, COLOR, textLabel
import time


def initialisation(maze):
    maze.states = {}
    maze.states = list(maze.maze_map.keys())

    maze.rewards = {}
    for state in maze.states:
        if state == (1, 1):
            maze.rewards[state] = 1
        else:
            maze.rewards[state] = -0.04

    maze.policy = {}
    for state in maze.states:
        maze.policy[state] = np.random.choice(possibleActions(maze, state))

    maze.valueMap = {}
    for state in maze.states:
        if state == (1, 1):
            maze.valueMap[state] = 10000
        else:
            maze.valueMap[state] = -1

    maze.threshold = 0.005
    maze.discount = 0.9


def possibleActions(maze, state):
    (x, y) = state
    actions = maze.maze_map[(x, y)]
    possibleStates = []
    for direction, bool in actions.items():
        if bool == 1:
            possibleStates.append(direction)
    return possibleStates


def getNextState(maze, currentState, action):
    if action == 'E':
        nextState = (currentState[0], currentState[1] + 1)
    elif action == 'W':
        nextState = (currentState[0], currentState[1] - 1)
    elif action == 'S':
        nextState = (currentState[0] + 1, currentState[1])
    elif action == 'N':
        nextState = (currentState[0] - 1, currentState[1])
    else:
        nextState = currentState
    if nextState in maze.states:
        return nextState
    else:
        return currentState


def valueIteration(maze):

    initialisation(maze)

    while True:
        delta = 0
        for state in maze.states:
            oldValue = maze.valueMap[state]
            max_value = float('-inf')
            for action in possibleActions(maze, state):
                nextState = getNextState(maze, state, action)
                v = maze.rewards[state] + (maze.discount * maze.valueMap[nextState])
                if v > max_value:
                    max_value = v
                    maze.policy[state] = action
            maze.valueMap[state] = max_value
            delta = max(delta, abs(oldValue - maze.valueMap[state]))
            #print(delta)
        if delta < maze.threshold:
            break

    return getPath(maze)


def getPath(maze):
    # print("Path start")
    path = []
    start = (maze.rows, maze.cols)
    current = start
    goal = (1, 1)
    path.append(current)
    while current != goal:
        action = maze.policy[current]
        current = getNextState(maze, current, action)
        path.append(current)
    # print("Path done")
    return path


if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze(loopPercent=50)
    start_time = time.time()
    valueIterationPath = valueIteration(m)
    end_time = time.time()
    # print(policyIterationPath)

    total_time_taken = end_time-start_time
    print(total_time_taken)

    cells_in_value_iteration_path = len(valueIterationPath)
    print(cells_in_value_iteration_path)

    Label1 = textLabel(m,"Total time taken", total_time_taken)
    Label3 = textLabel(m, "Shortest path", cells_in_value_iteration_path)

    a = agent(m, footprints=True, filled=False)
    m.tracePath({a: valueIterationPath}, delay=100)

    m.run()
