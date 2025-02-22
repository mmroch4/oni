[n, m, k] = input().split()
n = int(n)
m = int(m)
k = int(k)

directions = ['N', 'E', 'S', 'W']

planes = []
planes_directions = []

clouds = []

encounters = []

for i in range(n):
  [x, y] = input().split()
  x = int(x)
  y = int(y)
  
  planes.append([x, y])
  planes_directions.append('E')

for i in range(m):
  [x, y] = input().split()
  x = int(x)
  y = int(y)
  
  clouds.append([x, y])

for _ in range(k):
  for i in range(n):
    [x, y] = planes[i]
    d = planes_directions[i]
    
    new_coords = []
    
    match d:
      case 'N':
        # NORTH
        new_coords = [x, y - 1]
      case 'E':
        # EAST
        new_coords = [x + 1, y]
      case 'S':
        # SOUTH
        new_coords = [x, y + 1]
      case 'W':
        # WEST
        new_coords = [x - 1, y]
    
    if new_coords in clouds:
      direction_index = (directions.index(d) + 1) % len(directions)
      
      d = directions[direction_index]
      
      planes_directions[i] = d
    else:
      # count = planes.count(new_coords)

      # if 0 < count:
      #   planes_clone = planes.copy()
      #   left_length = 0
        
      #   for c in range(count):
      #     a = planes_clone.index(new_coords)
          
      #     is_in_encounters = ([i, a + left_length] in encounters) or ([a + left_length, i] in encounters)
          
      #     if not is_in_encounters:
      #       encounters.append([i, a + left_length])
          
      #     r = planes_clone[a + 1:]
      #     l = planes_clone[:a + 1]
          
      #     left_length += len(l)
          
      #     planes_clone = r
      count = planes.count(new_coords)

      if 0 < count:
        init = 0
                
        for c in range(count):
          a = planes.index(new_coords, init)
          is_in_encounters = ([i, a] in encounters) or ([a, i] in encounters)
          
          if not is_in_encounters:
            encounters.append([i, a])
          
          init = a + 1
      
      planes[i] = new_coords

print(len(encounters))