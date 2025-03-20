p = int(input())
n, k = map(int, input().split(' '))

def is_in_same_row(a, b, n):
  return a // n == b // n

if p == 1:
  sum_rows = dict()
  connected = False

  for i in range(k):
    r = int(input().split(' ')[0]) - 1
    
    if connected:
      print('Sim')
      continue
    
    if r not in sum_rows:
      sum_rows[r] = 0
    
    sum_rows[r] += 1
    
    if sum_rows[r] >= n:
      connected = True

    if connected:
      print('Sim')
    else:
      print('Nao')
else:
  sets = dict()
  
  for i in range(k):    
    r, c = map(int, input().split(' '))
    r -= 1
    c -= 1
    
    num_coords = c + r * n
    
    sets[num_coords] = -1
    
    neighbors = []
    
    up = num_coords - n
    down = num_coords + n
    right = num_coords + 1
    left = num_coords - 1
    
    if 0 <= up and up in sets:
      neighbors.append(up)
      
    if down <= n ** 2 - 1 and down in sets:
      neighbors.append(down)

    if is_in_same_row(num_coords, right, n) and right in sets:
      neighbors.append(right)
    
    if is_in_same_row(num_coords, left, n) and left in sets:
      neighbors.append(left)

    def find(a):
      if sets[a] < 0:
        return a
      
      sets[a] = find(sets[a])
      
      return sets[a]

    def unite(a, b):
      x, y = find(a), find(b)
      
      if x != y:
        if -sets[x] < -sets[y]:
          x, y = y, x
        
        sets[x] += sets[y]
        sets[y] = x

    for neighbor in neighbors:
      if neighbor in sets:
        unite(num_coords, neighbor)

    islands = i + 1

    for position in sets:
      v = sets[position]
      
      if v < -1:
        islands += v + 1
    
    print(islands)
