p = int(input())
[n, k] = input().split(' ')
n = int(n)
k = int(k)

cards = list(range(1, n + 1))

for _ in range(k):
  if p == 1:
    [a, b] = input().split(' ')
    a = int(a)
    b = int(b)
    
    [cards[a - 1], cards[b - 1]] = [cards[b - 1], cards[a - 1]]
  else:
    x = int(input())
    
    left = cards[0:x]
    right = cards[x:2*x]
    rest = cards[2*x:len(cards)]
    
    tempo = []
    
    for i in range(x):
      tempo.append(left[i])
      tempo.append(right[i])
    
    cards = tempo + rest

for i in range(n):
  print(cards[i])