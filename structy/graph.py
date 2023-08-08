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

# print(shortest_path(edges, 'w', 'z'))

def island_count(grid):
	visited = set()
	count = 0
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == "L" and (r, c) not in visited:
				count += 1
				visited.add((r, c))
				stack = [(r, c)]
				while stack:
					r, c = stack.pop()
					for neigh_adj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
						nr = neigh_adj[0] + r
						nc = neigh_adj[1] + c
						is_on_grid = 0 <= nc < len(grid[0]) and 0 <= nr < len(grid)
						if (nr, nc) not in visited and is_on_grid and grid[nr][nc] == "L":
							visited.add((nr, nc))
							stack.append((nr, nc))

	return count


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

# print(island_count(grid)) # -> 3



# def minimum_island(grid):
#   min_size = len(grid) * len(grid[0])
#   visited = set()

#   for r in range(len(grid)):
#     for c in range(len(grid[0])):
#       if grid[r][c] == "L" and (r, c) not in visited:
#         size = 0
#         visited.add((r, c))
#         stack = [(r, c)]
#           while stack:
#             cr, cc = stack.pop()
#             size += 1
#             for adjappend((nr, nc))
#                 visite in [[0,1],[1,0],[0,-1],[-1,0]]:
#               nr = cr + adj[0]
#               nc = cc + adj[1]
#               on_grid = 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
#               if on_grid and grid[nr][nc] == "L" and (nr, nc) not in visited:
#                 stack.d.add((nr, nc))
#       min_size = min(min_size, size)

#   return min_size
  

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

# print(minimum_island(grid))

def closest_carrot(grid, starting_row, starting_col):
  visited = set((starting_row, starting_col))
  queue = deque([(starting_row, starting_col, 0)])
  neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  while queue:
    print(queue)
    curr_row, curr_col, level = queue.popleft()
    print(curr_row, curr_col, grid[curr_row][curr_col])
    if grid[curr_row][curr_col] == "C":
      return level
    for neighbor in neighbors:
      neigh_row = curr_row + neighbor[0]
      neigh_col = curr_col + neighbor[1]
      on_grid = 0 <= neigh_col < len(grid[0]) and 0 <= neigh_row < len(grid)
      if on_grid and grid[neigh_row][neigh_col] == "O" and (neigh_row, neigh_col) not in visited:
        visited.add((neigh_row, neigh_col))
        queue.append((neigh_row, neigh_col, level + 1))
        
  return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

# print(closest_carrot(grid, 1, 2)) # -> 4


from collections import defaultdict

def semesters_required(num_courses, prereqs):
  graph = convert_to_adjacency_list(prereqs)
  distance = {}
  
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
  for node in graph:
    traverse_distance(graph, node, distance)
  return max(distance.values()) + 1 

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  max_length = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    max_length = max(max_length, attempt)
  
  distance[node] = 1 + max_length
  return distance[node]


def convert_to_adjacency_list(prereqs):
  graph = defaultdict(list) 
  for prereq, course in prereqs:
    graph[prereq].append(course)
    if course not in graph:
      graph[course] = []
  return graph

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
# print(semesters_required(num_courses, prereqs)) # -> 3


def best_bridge(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L":
        island = set()
        traverse_island(grid, r, c, island)
        break

  queue = deque([])
  visited = set(island)
  for pos in island:
    r, c = pos
    queue.append((r, c, 0))

  while queue:
    cr, cc, level = queue.popleft()
    if grid[cr][cc] == "L" and (cr, cc) not in island:
      return level - 1
    else:
      for neigh_pos in [[1,0], [0, 1],[-1,0], [0, -1]]:
        nr = cr + neigh_pos[0]
        nc = cc + neigh_pos[1]
        if is_in_bounds(grid, nr, nc) and (nr, nc) not in visited:
          visited.add((nr, nc))
          queue.append((nr, nc, level + 1))


def is_in_bounds(grid, row, col):
  row_check = 0 <= row < len(grid)
  col_check = 0 <= col < len(grid[0])
  return row_check and col_check

def traverse_island(grid, row, col, visited = set()):
  if not is_in_bounds(grid, row, col) or grid[row][col] == "W":
    return visited
    
  if (row, col) in visited:
    return visited
  
  visited.add((row, col))
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row, col + 1, visited)
  traverse_island(grid, row, col - 1, visited)

  return visited


grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["L", "L", "W", "W", "L"],
  ["W", "L", "W", "W", "L"],
  ["W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W"],
]
# print(best_bridge(grid)) # -> 1
# print(traverse_island(grid, 0, 3))


def has_cycle(graph):
  grey = set()
  black = set()
  
  for node in graph:
    if node not in grey and node not in black:
      stack = [node]
      while stack:
        curr = stack.pop()
        print(curr)
        print(grey)
        if curr in grey: return True
        grey.add(curr)
        for neighbor in graph[curr]:
          if neighbor not in black:
            stack.append(neighbor)

        
      black.add(node)
  return False


# print(has_cycle({
#   "a": ["b", "c"],
#   "b": ["c"],
#   "c": ["d"],
#   "d": [],
# })) # -> True


def longest_path(graph):
  max_path = 0 
  distance = {}
  for node, neighbors in graph.items():
    if len(graph[node]) == 0:
      distance[node] = 0
    
  for node in graph:
    attempt = traverse_graph(graph, node, distance)
    max_path = max(max_path, attempt)
    
  return max_path

def traverse_graph(graph, node, distance):
  print(distance)
  if node in distance: return distance[node]
  
  for neighbor in graph[node]:
    traverse_graph(graph, neighbor, distance)
    
  distance[node] = 1 + max(distance.values())
  
  return distance[node]


graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print(longest_path(graph))