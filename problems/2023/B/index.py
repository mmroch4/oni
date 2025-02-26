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

if p == 1:
  for a in range(t):
    pipe_limits = pipes[a]

    n = len(pipe_limits)

    is_possible = True
    first_moves = []
    restriction = []

    for i in range(n):
      pipe = pipe_limits[i]

      if i == 0:
        restriction = pipe
        first_moves = pipe

        continue
      
      movement_projection = [restriction[0] + 1, restriction[1] + 1]

      intersec = intersection(pipe, movement_projection)

      if intersec == False:
        is_possible = False
        break
      
      restriction = intersec
      
      f = intersection(pipe, [first_moves[0] + i, first_moves[1] + i])

      if f == False:
        is_possible = False
        break
      
      first_moves = [f[0] - i, f[1] - i]

    if is_possible:
      moves = list(range(first_moves[0], first_moves[0] + n))

      print('SIM')
      print(' '.join(map(str, moves)))
    else:
      print('NAO')
else:
  for a in range(t):
    pipe_limits = pipes[a]

    n = len(pipe_limits)

    if n == 1:
      print('SIM')
      print(pipe_limits[0][1])
      continue

    is_possible = True
    restriction = []
    
    choke_points = []

    for i in range(n):      
      pipe = pipe_limits[i]
      
      if i == 0:
        restriction = pipe
      else:
        movement_projection = [restriction[0] - 1, restriction[1] + 1]

        intersec = intersection(pipe, movement_projection)

        if intersec == False:
          is_possible = False
          break

        restriction = intersec
      
      choke_points.append(restriction)
      
      # backwards = intersection(restriction, [intersec[0] - 1, intersec[1] + 1])

      # if i != 0:   
      #   moves_rules.append(backwards)
      
      # if i == n - 1:
      #   moves_rules.append(intersec)
      #   print(i + 1, 'BACKWARDS', intersec)
      
      # restriction = intersec 

    # for i in range(len(choke_points) - 1, -1, -1):
    #   if i == n - 1:
    #     continue
    #   print(i)
    #   previous = choke_points[i]
    #   current = choke_points[i]
      
    #   #print(choke_points[i], i)
      
    #   o = intersection(previous, current)
    #   #print(i, 'AQUI', o)
    
    if is_possible:
      b = len(choke_points) - 1

      while 0 <= b:
        if b == n - 1:
          b -= 1
          continue

        previous = choke_points[b + 1]
        current = choke_points[b]
        
        intersec = intersection(current, [previous[0] - 1, previous[1] + 1])

        choke_points[b] = intersec

        b -= 1

      moves = []

      for choke_point in choke_points:
        moves.append(str(choke_point[0]))
        
      print('SIM')
            
      #print(moves)
      print(' '.join(moves))
    else:
      print('NAO')