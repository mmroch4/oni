p = int(input())
n, k = map(int, input().split(' '))

counters = [0] * k

if p == 3:
  votes = []

  for i in range(n):
    vote = list(map(int, (input().split(' '))))
    
    votes.append(vote)

  for r in range(k):
    for i in range(n):
      vote = int(votes[i][r])
      
      counters[vote - 1] += 1

    winners = []
    winner_counter = 0
    
    for i in range(k):
      counter = counters[i]
      
      if winner_counter < counter:
        winner_counter = counter
        winners.clear()
        winners.append(i + 1)
      elif winner_counter == counter:
        winners.append(i + 1)
    
    if 1 < len(winners):
      continue
    else:
      print(winners[0])
      break
else: 
  votes = input().split(' ')

  for i in range(n):
    vote = int(votes[i])
    
    counters[vote - 1] += 1

  if p == 2:
    print(' '.join(list(map(str, counters))))
  else:
    winners = []
    winner_counter = 0

    for i in range(k):
      counter = counters[i]
      
      if winner_counter < counter:
        winner_counter = counter
        winners.clear()
        winners.append(i + 1)
      elif winner_counter == counter:
        winners.append(i + 1)

    if 1 < len(winners):
      print(0)
    else:
      print(winners[0])
