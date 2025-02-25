import math

n, m = map(int, input().split(' '))

prices = list(map(int, input().split(' ')))
budgets = list(map(int, input().split(' ')))


prices.sort()

for i in range(n):
  if i == 0:
    continue
  
  prices[i] = prices[i] + prices[i - 1]

def binary_search(value, list, acc_index):
  list_length = len(list)
  
  i = math.floor(list_length / 2)
  
  if list_length == 1:
    return acc_index
  
  if list[i] == value:
    return acc_index + i
  elif list[i] < value:
    return binary_search(value, list[i:], acc_index + i)
  elif value < list[i]:
    return binary_search(value, list[:i], acc_index)

for budget in budgets:
  i = binary_search(budget, prices, 0)
  
  print(i + 1)
