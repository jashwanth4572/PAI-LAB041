from collections import deque

CAPACITY = (8, 5, 3)
GOAL = 4


def get_successors(state):
    A, B, C = state
    capA, capB, capC = CAPACITY
    successors = []

    successors.append((capA, B, C))
    successors.append((A, capB, C))
    successors.append((A, B, capC))

    successors.append((0, B, C))
    successors.append((A, 0, C))
    successors.append((A, B, 0))

    pour = min(A, capB - B)
    successors.append((A - pour, B + pour, C))

    pour = min(A, capC - C)
    successors.append((A - pour, B, C + pour))

    pour = min(B, capA - A)
    successors.append((A + pour, B - pour, C))

    pour = min(B, capC - C)
    successors.append((A, B - pour, C + pour))

    pour = min(C, capA - A)
    successors.append((A + pour, B, C - pour))

    pour = min(C, capB - B)
    successors.append((A, B + pour, C - pour))

    return successors


def bfs(initial_state):
    queue = deque([initial_state])
    visited = set([initial_state])
    parent = {initial_state: None}

    while queue:
        current = queue.popleft()

        if GOAL in current:
            return construct_path(parent, current)

        for next_state in get_successors(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None


def construct_path(parent, goal_state):
    path = []
    while goal_state is not None:
        path.append(goal_state)
        goal_state = parent[goal_state]
    path.reverse()
    return path

initial_state = (0, 0, 0)
solution = bfs(initial_state)

if solution:
    print("Solution found using BFS:")
    for step in solution:
        print(step)
else:
    print("No solution found")
