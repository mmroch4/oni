p = int(input())

if p == 1:
  n, k = map(int, (input().split(' ')))
else: 
  n, k, x = map(int, (input().split(' ')))

colors = list(map(int, input().split(' ')))

if 1 < n:
  counters = []
  counter = 0 

  for i in range(n + 1):
    if i == 0:
      counter = 1
      continue
    
    if i < n:
      previous = colors[i - 1]
      current = colors[i]
    
      if previous != current:
        counters.append(counter)
        counter = 1
      else:
        counter += 1
    else:
      counters.append(counter)

  if p == 1:
    print(len(counters))
  else:
    counters.sort()
    del counters[-x:]
  
    print(sum(counters))
else:
  if p == 1:
    print(1)
  else:
    print(0)