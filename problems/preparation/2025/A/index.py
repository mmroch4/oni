p = int(input())
n = int(input())

hours = [[] for _ in range(24)]

for _ in range(n):
  c, a, b = map(int, input().split(' '))

  for i in range(24):
    if a <= i <= b:
      hours[i].append(str(c))
    elif b < a and (a <= i or i <= b):
      hours[i].append(str(c))

print(hours)

' '.join(list(map(lambda x:len(x), hours)))