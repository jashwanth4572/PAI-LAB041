import heapq

CAP_A = 4
CAP_B = 3
GOAL = 2

def heuristic(state):
    """Admissible heuristic"""
    a, b = state
    return min(abs(a - GOAL), abs(b - GOAL))

def get_successors(state):
    a, b = state
    successors = []

    successors.append((CAP_A, b))
    successors.append((a, CAP_B))

    successors.append((0, b))
    successors.append((a, 0))

    pour = min(a, CAP_B - b)
    successors.append((a - pour, b + pour))

    pour = min(b, CAP_A - a)
    successors.append((a + pour, b - pour))

    return successors

def a_star(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start))
    parent = {start: None}
    g_cost = {start: 0}
    closed = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if GOAL in current:
            return reconstruct_path(parent, current)

        closed.add(current)

        for nxt in get_successors(current):
            if nxt in closed:
                continue

            new_g = g + 1
            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                f_cost = new_g + heuristic(nxt)
                heapq.heappush(open_list, (f_cost, new_g, nxt))
                parent[nxt] = current

    return None

def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path

start_state = (0, 0)
solution = a_star(start_state)

if solution:
    print("Solution using A* Search:")
    for step in solution:
        print(step)
else:
    print("No solution found")
