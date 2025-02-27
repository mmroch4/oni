p = int(input())
t = int(input())

pipes = []

for a in range(t):
  pipes.append([])
  
  n = int(input())
  
  for b in range(n):
    l, r = map(int, input().split(' '))
    
    pipes[a].append([l, r])

def intersection(a, b):
  [a_start, a_end] = a
  [b_start, b_end] = b
  
  if a_start - b_end <= 0 and 0 <= a_end - b_start:    
    start = a_start if 0 <= a_start - b_start else b_start
    end = a_end if 0 <= b_end - a_end else b_end
    
    return [start, end]
  
  return False

for a in range(t):
  limits = pipes[a]

  n = len(limits)
  
  if n == 1:
    print('SIM')
    print(limits[0][1])
    continue

  is_possible = True
  restriction = []

  choke_points = []

  for i in range(n):
    pipe = limits[i]

    if i == 0:
      restriction = pipe
    else:
      movement_projection = [restriction[0] + 1, restriction[1] + 1] if p == 1 else [restriction[0] - 1, restriction[1] + 1]

      intersec = intersection(pipe, movement_projection)

      if intersec == False:
        is_possible = False
        break

      restriction = intersec
    
    choke_points.append(restriction)

  if is_possible:
    b = len(choke_points) - 1

    while 0 <= b:
      current = choke_points[b]
      
      if b == n - 1:
        b -= 1
        continue

      previous = choke_points[b + 1]
      
      movement_projection = [previous[0] - 1, previous[1] - 1] if p == 1 else [previous[0] - 1, previous[1] + 1]

      intersec = intersection(current, movement_projection)

      choke_points[b] = intersec

      b -= 1

    moves = []

    for choke_point in choke_points:
      moves.append(str(choke_point[0]))

    print('SIM')
    print(' '.join(moves))
  else:
    print('NAO')