from pyamaze import maze, agent, textLabel
import numpy as np
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

    maze.valueMap = {}
    for state in maze.states:
        maze.valueMap[state] = 0

    maze.transitions = {}
    for state in maze.states:
        maze.transitions[state] = {}
        for action in possibleActions(maze, state):
            nextState = getNextState(maze, state, action)
            if nextState == state:
                maze.transitions[state][action] = [(1, nextState)]
            else:
                maze.transitions[state][action] = [(0.9, nextState), (0.1, state)]

    maze.policy = {}
    for state in maze.states:
        maze.policy[state] = {np.random.choice(possibleActions(maze, state)): 1}

    maze.gamma = 0.99
    maze.theta = 1e-3


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


def policyEvaluation(maze):
    # print("Eval start")
    while True:
        delta = 0
        for state in maze.states:
            v = 0
            for action, actionProb in maze.policy[state].items():
                for prob, nextState in maze.transitions[state][action]:
                    v += actionProb * prob * (maze.rewards[nextState] + maze.gamma * maze.valueMap[nextState])
            delta = max(delta, abs(v - maze.valueMap[state]))
            maze.valueMap[state] = v
        if delta < maze.theta:
            break
    # print("Eval done")


def policyImprovement(maze):
    policyStable = True
    for state in maze.states:
        oldAction = max(maze.policy[state], key=maze.policy[state].get)
        newAction = None
        maxValue = float('-inf')
        for action in possibleActions(maze, state):
            v = 0
            for prob, nextState in maze.transitions[state][action]:
                v += prob * (maze.rewards[nextState] + maze.gamma * maze.valueMap[nextState])
            if v > maxValue:
                maxValue = v
                newAction = action
        maze.policy[state] = {newAction: 1}
        if oldAction != newAction:
            policyStable = False
    return policyStable


def getPath(maze):
    # print("Path start")
    path = []
    start = (maze.rows, maze.cols)
    current = start
    goal = (1, 1)
    path.append(current)
    while current != goal:
        action = max(maze.policy[current], key=maze.policy[current].get)
        current = getNextState(maze, current, action)
        path.append(current)
    # print("Path done")
    return path


def policyIteration(maze):
    initialisation(maze)
    while True:
        policyEvaluation(maze)
        if policyImprovement(maze):
            break
    return getPath(maze)


if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze(loopPercent=50)
    start_time = time.time()
    policyIterationPath = policyIteration(m)
    end_time = time.time()
    # print(policyIterationPath)

    total_time_taken = end_time-start_time
    print(total_time_taken)

    cells_in_policy_iteration_path = len(policyIterationPath)
    print(cells_in_policy_iteration_path)

    Label1 = textLabel(m,"Total time taken", total_time_taken)
    Label3 = textLabel(m, "Shortest path", cells_in_policy_iteration_path)

    a = agent(m, footprints=True, filled=False)
    m.tracePath({a: policyIterationPath}, delay=100)

    m.run()
