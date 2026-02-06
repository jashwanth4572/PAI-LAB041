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


def dfs(state, visited, path):
    
    if GOAL in state:
        path.append(state)
        return True

    visited.add(state)
    path.append(state)

    for next_state in get_successors(state):
        if next_state not in visited:
            if dfs(next_state, visited, path):
                return True

    path.pop()
    return False

initial_state = (0, 0, 0)
visited = set()
path = []

found = dfs(initial_state, visited, path)

if found:
    print("Solution found using DFS:")
    for step in path:
        print(step)
else:
    print("No solution found")
