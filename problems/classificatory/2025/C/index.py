p = int(input())
t = int(input())

def convert_coords_to_index(coords, n):
  row = coords // n
  col = coords - row * n
  
  return (row, col)

def get_adjacents(coords, n, grid, visited):
  neighbors = []
    
  up = coords - n
  down = coords + n
  right = coords + 1
  left = coords - 1
  
  i_up = convert_coords_to_index(up, n)
  i_down = convert_coords_to_index(down, n)
  i_right = convert_coords_to_index(right, n)
  i_left = convert_coords_to_index(left, n)
  
  if 0 <= up and grid[i_up[0]][i_up[1]] == '.' and up not in visited:
    neighbors.append(up)
    
  if down <= n ** 2 - 1 and grid[i_down[0]][i_down[1]] == '.' and down not in visited:
    neighbors.append(down)

  if is_in_same_row(coords, right, n) and grid[i_right[0]][i_right[1]] == '.' and right not in visited:
    neighbors.append(right)
  
  if is_in_same_row(coords, left, n) and grid[i_left[0]][i_left[1]] == '.' and left not in visited:
    neighbors.append(left)
  
  return neighbors

def get_adjacents_3(coords, n, grid):
  neighbors = []
    
  up = coords - n
  down = coords + n
  right = coords + 1
  left = coords - 1
  
  i_up = convert_coords_to_index(up, n)
  i_down = convert_coords_to_index(down, n)
  i_right = convert_coords_to_index(right, n)
  i_left = convert_coords_to_index(left, n)
  
  if 0 <= up and grid[i_up[0]][i_up[1]] == '.':
    neighbors.append(up)
    
  if down <= n ** 2 - 1 and grid[i_down[0]][i_down[1]] == '.':
    neighbors.append(down)

  if is_in_same_row(coords, right, n) and grid[i_right[0]][i_right[1]] == '.':
    neighbors.append(right)
  
  if is_in_same_row(coords, left, n) and grid[i_left[0]][i_left[1]] == '.':
    neighbors.append(left)
  
  return neighbors


def is_in_same_row(a, b, n):
  return a // n == b // n

if p == 1:
  while t:
    t -= 1
    
    n, k = map(int, input().split(' '))
    
    a_r, a_c = map(int, input().split(' '))
    a_r -= 1
    a_c -= 1
    a_coords = a_c + a_r * n
    
    b_r, b_c = map(int, input().split(' '))
    b_r -= 1
    b_c -= 1
    b_coords = b_c + b_r * n
    
    grid = []
    
    for _ in range(n):
      row = input()
      grid.append(row)
    
    visited = set([a_coords])
    adjacents = get_adjacents(a_coords, n, grid, visited)

    def search(adjacents, depth, to_find, limit, n, grid):
      adjs = set()

      for adjacent in adjacents:
        # print('VISITING', adjacent, depth)
        visited.add(adjacent)

        if adjacent == to_find:
          return True
        
        for adj in get_adjacents(adjacent, n, grid, visited):
          adjs.add(adj)
      
      if len(adjs) == 0:
        return False
      
      return search(adjs, depth + 1, to_find, limit, n, grid)
    
    is_possible = search(adjacents, 1, b_coords, k, n, grid)

    print(['NAO', 'SIM'][is_possible])
    
elif p == 2:
  while t:
    t -= 1
    
    n, k = map(int, input().split(' '))
    
    a_r, a_c = map(int, input().split(' '))
    a_r -= 1
    a_c -= 1
    a_coords = a_c + a_r * n
    
    b_r, b_c = map(int, input().split(' '))
    b_r -= 1
    b_c -= 1
    b_coords = b_c + b_r * n
    
    grid = []
    
    for _ in range(n):
      row = input()
      grid.append(row)
    
    visited = set([a_coords])
    adjacents = get_adjacents(a_coords, n, grid, visited)

    def search(adjacents, depth, to_find, limit, n, grid):
      adjs = set()

      for adjacent in adjacents:
        # print('VISITING', adjacent, depth)
        visited.add(adjacent)

        if adjacent == to_find and depth <= limit:
          return True
        
        for adj in get_adjacents(adjacent, n, grid, visited):
          adjs.add(adj)
      
      if len(adjs) == 0:
        return False

      if depth >= limit:
        return False
      
      return search(adjs, depth + 1, to_find, limit, n, grid)
    
    is_possible = search(adjacents, 1, b_coords, k, n, grid)

    print(['NAO', 'SIM'][is_possible])
    
else:
  while t:
    t -= 1
    
    n, k = map(int, input().split(' '))
    
    a_r, a_c = map(int, input().split(' '))
    a_r -= 1
    a_c -= 1
    a_coords = a_c + a_r * n
    
    b_r, b_c = map(int, input().split(' '))
    b_r -= 1
    b_c -= 1
    b_coords = b_c + b_r * n
    
    grid = []
    
    for _ in range(n):
      row = input()
      grid.append(row)
    
    visited = set([a_coords])
    adjacents = get_adjacents(a_coords, n, grid, visited)

    m = -1

    def search(adjacents, depth, to_find, limit, n, grid):
      global m
      adjs = set()

      for adjacent in adjacents:
        # print('VISITING', adjacent, depth)
        visited.add(adjacent)

        if adjacent == to_find:
          m = depth
          return True
        
        for adj in get_adjacents(adjacent, n, grid, visited):
          adjs.add(adj)
      
      if len(adjs) == 0:
        return False
      
      return search(adjs, depth + 1, to_find, limit, n, grid)
    
    is_possible = search(adjacents, 1, b_coords, k, n, grid)
    
    is_possible_in_k_tries = (k - m) % 2 == 0 if is_possible else False

    print(['NAO', 'SIM'][is_possible_in_k_tries])
    