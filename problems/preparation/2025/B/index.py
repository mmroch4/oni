p = int(input())
n = int(input())

conversion = {
  "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
  "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
  "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
}

players = input()
converted_players = []

for player in players:
  converted_players.append(conversion[player])

if p == 1:
  raw_counters = [[] for _ in range(26)]

  i = 0

  while i < n:
    case_index = converted_players[i] - 1
    
    if len(raw_counters[case_index]) == 2:
      raw_counters[case_index][1] = i
    else:
      raw_counters[case_index] = [i, i]

    i += 1

  counters = list(filter(lambda x:len(x), raw_counters))

  for u in range(len(counters)):
    a = counters[u]
    
    for k in range(len(counters)):
      if u == k:
        continue
      
      b = counters[k]
      
      if a[0] - b[1] <= 0 and 0 <= a[1] - b[0]:
        start = a[0] if a[0] <= b[0] else b[0]
        end = a[1] if b[1] <= a[1] else b[1]
        
        new_range = [start, end]
        
        counters[u] = new_range
        counters[k] = new_range

  teams = []

  for u in range(len(counters)):
    a = counters[u]
    
    if a not in teams:
      teams.append(a)

  print(len(teams))
else:
  s = set()
  counter = 1
  
  for player in converted_players:
    if player in s:
      s.clear()
      counter += 1
      s.add(player)
    else:
      s.add(player)
      
  print(counter)