[a, l, c] = input().split(' ')
a = int(a)
l = int(l)
c = int(c)


if a >= 3 and a * l * c >= 50:
  print(1)
else:
  print(0)