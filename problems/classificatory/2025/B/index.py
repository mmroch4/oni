p = int(input())
n, k = map(int, input().split(' '))

PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def mmc(nums, num_size):
  prime_number_i = 0
  
  acc = 1
  
  ones = 0
  
  while ones < num_size:
    can_change_prime_number = 0
    
    acc_round = 1
    
    for i in range(num_size):
      num = nums[i]
      
      if num == 1:
        continue
      
      if num % PRIME_NUMBERS[prime_number_i] == 0:
        nums[i] /= PRIME_NUMBERS[prime_number_i]
        acc_round = PRIME_NUMBERS[prime_number_i]
        
        if nums[i] == 1:
          ones += 1
      else:
        can_change_prime_number += 1
    
    acc *= acc_round
    
    if can_change_prime_number == num_size - ones:
      prime_number_i += 1
  
  return acc

if p == 1:
  signals = []
  
  for _ in range(k):
    x = int(input())
    
    if x != 1:
      signals.append(x)

  print(mmc(signals, len(signals)))
else:
  signals = []

  j = 0

  while j < k:
    [x, p, s] = input().split(' ')
    
    signals.append((int(x), s))
    
    j += 1

  signals.sort()

  acc_seconds = 0

  i = 0

  while i < k:
    signal = signals[i]
    
    acc = signal[0] + acc_seconds
    
    light = signal[1][acc % len(signal[1])]
    
    if light == 'd':
      i += 1
    else:
      acc_seconds += 1

  print(n + acc_seconds)
