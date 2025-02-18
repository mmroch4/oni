n = int(input())
heights = input().strip().split()

counter = 0
max_h = 0

for h in heights:
  h = int(h)
  
  if h > max_h:
    max_h = h
    counter += 1

print(counter)