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

# print(has_path(graph, 'f', 'k')) # True



def connected_components_count(graph):
    visited = set()
    count = 0
    for node, edges in graph.items():
        if node not in visited:
            count += 1

            stack = [node]
            while stack:
                print(stack)
                curr = stack.pop()
                visited.add(curr)
                for cn in graph[curr]:
                    if cn not in visited:
                        stack.append(cn)
            
    return count


# print(connected_components_count({
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# })) # -> 2



def largest_component(graph):
	max_node = 0
	visited = set()
	
	for node, edges in graph.items():
		if node not in visited:
			node_count = 0
			visited.add(node)      
			stack = [node]
			while stack:
				curr = stack.pop()
				print(graph[curr])
				node_count += 1
				for neighbor in graph[curr]:
					if neighbor not in visited:
						visited.add(neighbor)
						stack.append(neighbor)
		max_node = max(max_node, node_count)
	
	return max_node


# print(largest_component({
#   3: [],
#   4: [6],
#   6: [4, 5, 7, 8],
#   8: [6],
#   7: [6],
#   5: [6],
#   1: [2],
#   2: [1]
# })) # -> 6


from collections import defaultdict
from collections import deque

def shortest_path(edges, node_A, node_B):
  adj_dict = defaultdict(list)
  
  for neighbors in edges:
    adj_dict[neighbors[0]].append(neighbors[1])
    adj_dict[neighbors[1]].append(neighbors[0])
    
  visited = set(node_A)
  queue = deque([(node_A, 0)])

  while queue:
    curr, level = queue.popleft()
    if curr == node_B:
      return level
    
    for neighbor in adj_dict[curr]:
      if neighbor not in visited:
        queue.append((neighbor, level + 1))
        visited.add(neighbor)
        
  return -1
  
    
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))