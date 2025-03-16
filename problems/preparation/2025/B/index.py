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

  def remove_empty(a):
    if len(a):
      return True
    
    return False

  counters = list(filter(remove_empty, raw_counters))

  def does_intersect(a, b):
    [a_start, a_end] = a
    [b_start, b_end] = b
    
    if a_start - b_end <= 0 and 0 <= a_end - b_start:    
      return True
    
    return False

  def combine_ranges_by_lowest_and_biggest(a, b):
    start = a[0] if a[0] <= b[0] else b[0]
    end = a[1] if b[1] <= a[1] else b[1]
    
    return [start, end]

  for u in range(len(counters)):
    a = counters[u]
    
    for k in range(len(counters)):
      if u == k:
        continue
      
      b = counters[k]
      
      if does_intersect(a, b):
        new_range = combine_ranges_by_lowest_and_biggest(a, b)
        
        counters[u] = new_range
        counters[k] = new_range

  teams = []

  for u in range(len(counters)):
    a = counters[u]
    
    if a not in teams:
      teams.append(a)

  print(len(teams))
else:
  # TODO
  print('TODO')