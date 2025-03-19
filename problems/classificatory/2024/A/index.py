p = int(input())
n, k = map(int, input().split(' '))

cards = list(range(1, n + 1))

if p == 1:
  while k:
    k -= 1
    
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    
    backup = cards[a]
    cards[a] = cards[b]
    cards[b] = backup
    
  for card in cards:
    print(card)
else:
  while k:
    k -= 1
    
    s = int(input())
    
    rest = cards[2 * s:]
    aux = []
    
    i = 0
    
    while i < s:
      aux.append(cards[i])
      aux.append(cards[i + s])
      
      i += 1
    
    aux.extend(rest)
    cards = aux.copy()
  
  for card in cards:
    print(card)