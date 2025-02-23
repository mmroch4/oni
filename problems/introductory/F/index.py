n = int(input())
n_cards = input().split(' ')
m = int(input())
m_cards = input().split(' ')

def get_even_odd_amount(list):
  even = 0
  odd = 0

  for el in list:    
    if int(el) % 2 == 0:
      even += 1
    else:
      odd += 1 
  
  return [even, odd]

[n_even, n_odd] = get_even_odd_amount(n_cards)
[m_even, m_odd] = get_even_odd_amount(m_cards)

count_odd = n_odd * m_even + n_even * m_odd
count_even = n_odd * m_odd + n_even * m_even

print(count_even, count_odd)