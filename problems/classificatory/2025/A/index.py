p = int(input())
n = int(input())

LOWER_A_LIMIT = ord('a')
LOWER_Z_LIMIT = ord('z')

UPPER_A_LIMIT = ord('A')
UPPER_Z_LIMIT = ord('Z')

DISTANCE_UPPER_TO_LOWER = LOWER_A_LIMIT - UPPER_A_LIMIT 

def identify_case_format(word):
  # 0 -> snake_case / 1 -> kebab-case / 2 -> dromedaryCase / 3 -> PascalCase
  if UPPER_A_LIMIT <= ord(word[0]) <= UPPER_Z_LIMIT:
    return 3 # PascalCase
  
  for c in word:
    if c == '_':
      return 0 # snake_case
    elif c == '-':
      return 1 # kebab-case

  return 2 # dromedaryCase

def lowerToUpper(char):
  return chr(ord(char) - DISTANCE_UPPER_TO_LOWER)

def upperToLower(char):
  return chr(ord(char) + DISTANCE_UPPER_TO_LOWER)

if p == 1:
  uppercases = [0 for _ in range(26)]
  
  while n:
    n -= 1
    
    word = input()

    for c in word:
      o = ord(c)
      
      if UPPER_A_LIMIT <= o <= UPPER_Z_LIMIT:
        i = o - UPPER_A_LIMIT
        
        uppercases[i] = True
  
  ans = []
  i = 0
  
  while i < 26:
    h = uppercases[i]
    
    if uppercases[i]:
      ans.append(chr(i + LOWER_A_LIMIT))
    
    i += 1
  
  print(' '.join(ans))
elif p == 2:
  while n:
    n -= 1
    
    word = input()

    print(['snake_case', 'kebab-case', 'dromedaryCase', 'PascalCase'][identify_case_format(word)])
else:
  while n:
    n -= 1
    
    word = input()
    
    # 0 -> snake_case / 1 -> kebab-case / 2 -> dromedaryCase / 3 -> PascalCase
    case_format = identify_case_format(word)

    if case_format == 2:
      # dromedaryCase
      print(word)
    elif case_format == 0:
      # snake_case
      parts = word.split('_')

      i = 1
      
      while i < len(parts):
        s = parts[i]
        
        first_char = lowerToUpper(s[0])
        
        parts[i] = first_char + s[1:]
        
        i += 1
      
      print(''.join(parts))
    elif case_format == 1:
      # kebab-case
      parts = word.split('-')
      i = 1
      
      while i < len(parts):
        s = parts[i]
        
        first_char = lowerToUpper(s[0])
        
        parts[i] = first_char + s[1:]
        
        i += 1
      
      print(''.join(parts))
    else:
      # PascalCase
      first_char = upperToLower(word[0])

      print(first_char + word[1:])