p = int(input())
t = int(input())

def isBipartite(n, v):
  groups = [-1] * n
  
  groups[0] = 0
  
  l = [0]
  
  while l:
    h = l.pop(0)
    
    for a in v[h]:
      if groups[a] == -1:
        groups[a] = 1 - groups[h]
        l.append(a)

      elif groups[a] == groups[h]:
        return False
  
  return True

while t:
  t -= 1

  n, m = map(int, input().split(' '))

  v = [[] for _ in range(n)]

  for i in range(m):
    a, b  = map(int, input().split(' '))
    
    v[a - 1].append(b - 1)
    v[b - 1].append(a - 1)
  
  if isBipartite(n, v):
    print("sim")
  else:
    print("nao")