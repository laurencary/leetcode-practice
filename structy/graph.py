def has_path(graph, src, dst):
    # print(graph[src])
    if src == dst: return True
    for path in graph[src]:
        # print(path)
        # print(graph[path])
        if len(graph[src]) > 0:
            if has_path(graph, path, dst) == True:
                return True
    
    return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k')) # True