p = int(input())
t = int(input())

def convert_name_to_graph(name):
  return (ord(name[0]), ord(name[-1]))

A_TO_INT = ord('a')
Z_TO_INT = ord('z')

while t:
  t -= 1
  
  n = int(input())
  names = input().split(' ')
  
  if n == 1:
    print('Nao')
    
    continue
  
  graphs = list(map(convert_name_to_graph, names))

  can_combine = False
  
  if p == 1:
    starts_by_a_ends = set()
    ends_by_z_starts = set()

    for i in range(n):
      graph = graphs[i]
      
      if graph[0] == A_TO_INT:
        starts_by_a_ends.add(graph[1])
      
      if graph[1] == Z_TO_INT:
        ends_by_z_starts.add(graph[0])

    for v in starts_by_a_ends:
      if v in ends_by_z_starts:
        can_combine = True
        break

    if can_combine:
      print('Sim')
    else:
      print('Nao')
  else:
    connections = dict()
    
    for i in range(n):
      graph = graphs[i]
      
      if graph[0] not in connections:
        connections[graph[0]] = set([graph[1]])
      else:
        connections[graph[0]].add(graph[1])
    
    if A_TO_INT not in connections:
      print('Nao')
      continue
    
    children = connections[A_TO_INT]
    
    checked = set()
    
    def check(parent):
      if parent in checked or parent not in connections:
        return False
      else:
        checked.add(parent)
      
      children = connections[parent]
      
      if Z_TO_INT in children:
        return True

      for child in children:
        if child in checked:
          continue
        
        if check(child):
          return True
      
      return False
    
    for child in children:
      if check(child):
        can_combine = True
        break
    
    if can_combine:
      print('Sim')
    else:
      print('Nao')