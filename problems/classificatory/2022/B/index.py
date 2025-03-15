p = int(input())

if p == 1:
  n, k = map(int, (input().split(' ')))
else: 
  n, k, x = map(int, (input().split(' ')))

colors = list(map(int, input().split(' ')))

if 1 < n:
  counters = []
  counter = 1

  for i in range(1, n):
    previous = colors[i - 1]
    current = colors[i]
  
    if previous != current:
      counters.append(counter)
      counter = 1
    else:
      counter += 1

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