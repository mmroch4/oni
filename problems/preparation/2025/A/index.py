import itertools

p = int(input())
n = int(input())

if p == 1:
  hours = [0] * 24

  for _ in range(n):
    c, a, b = map(int, input().split(' '))

    r = range(a, b + 1) if a <= b else itertools.chain(range(a, 24), range(b + 1))

    for i in r:
      hours[i] += 1 
      
  print(' '.join(list(map(str, hours))))
else:
  hours = input().split(' ')
  
  l = set(hours)
  
  print(len(l))