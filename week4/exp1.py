def is_valid(node, color, assignment, graph):
 
    return all(assignment.get(neigh) != color for neigh in graph[node])

def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment 
    node = next(n for n in graph if n not in assignment)
    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[node]  
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ['Red', 'Green', 'Blue']

solution = backtrack({}, graph, colors)
print("Solution:", solution)
