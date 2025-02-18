[n, k] = input().split(' ')
n = int(n)
k = int(k)

r = 0

for i in range(n):
  space = input()
  
  if 0 <= space.find('.'*k):
    r = 1
    
    break

print(r)