import bisect
import itertools

n, m = map(int, input().split(' '))

prices = list(map(int, input().split(' ')))
budgets = list(map(int, input().split(' ')))

prices.sort()

prices_sum = list(itertools.accumulate(prices))

# for i in range(n):
#   if i == 0:
#     continue
  
#   prices[i] = prices[i] + prices[i - 1]

# def binary_search(value, list, acc_index):
#   list_length = len(list)
  
#   i = list_length // 2
  
#   if list_length == 1:
#     return acc_index
  
#   if list[i] == value:
#     return acc_index + i
#   elif list[i] < value:
#     return binary_search(value, list[i:], acc_index + i)
#   elif value < list[i]:
#     return binary_search(value, list[:i], acc_index)

# def binary_search(value, list, left, right):
#   while left < right:
#     mid = (left + right) // 2

#     if mid == left:
#       return mid

#     if list[mid] == value:
#       return mid
#     elif list[mid] < value:
#       left = mid
#     elif value < list[mid]:
#       right = mid

for budget in budgets:
  print(bisect.bisect(prices_sum, budget))
