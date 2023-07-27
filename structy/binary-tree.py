class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_finder(root, target, path = []):
    if root.val == target: return path.append(root.val)
    if root.left is None and root.right is None: return None

    left, right = None, None
    if root.left is not None:
        left = path_finder(root.left, target, [*path,*root.val])
    if root.right:
        right = path_finder(root.right, target, [*path,*root.val])
    
    return left or right

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]

def all_tree_paths(root):
  if root.left is None and root.right is None:
    return [[root.val]]
  paths = []
  if root.left:
    paths = [*paths, *all_tree_paths(root.left)]
  if root.right:
    paths = [*paths, *all_tree_paths(root.right)]
  print(root.val)
  print(paths)
  for i in range(len(paths)):
    paths[i].insert(0, root.val)
  
  return paths

# print(all_tree_paths(a))


from collections import deque

def tree_levels(root):
    queue = deque([(root, 0)])
    levels = [[]]
    level = 0
    while queue:
        curr, level = queue.popleft()
        if level < len(levels):
            levels[level].append(curr.val)
        else:
            levels.append([curr.val])

        level += 1
        if curr.left:
            queue.append((curr.left, level))
        if curr.right:
            queue.append((curr.right, level))

    return levels

print(tree_levels(a))
