p = int(input())

[n,m] = input().split()
n = int(n)
m = int(m)

room = []

for i in range(n):
  l = input()

  room.append(l)

t = int(input())

for i in range(t):
  x = 0
  y = 0
  auto = False
  cycle = False
  history = []
  
  k = int(input())
  commands = input()
  
  def right():
    move(x + 1, y, x + 1 < m) # RIGHT

  def left():
    move(x - 1, y, 0 <= x - 1) # LEFT

  def up():
    move(x, y - 1, 0 <= y - 1) # UP

  def down():
    move(x, y + 1, y + 1 < n) # DOWN

  def move(_x, _y, is_valid):
    global auto, cycle, x, y
    if not is_valid or room[_y][_x] == '#':
      auto = False
      return
    
    x = _x
    y = _y
    
    if p == 2:
      s = room[y][x]
    
      if s in ['D', 'B', 'C', 'E']:
        auto = s

        if (x,y) in history:
          cycle = True
          return

        history.append((x,y))

      match auto:
        case 'D':
          right()
        case 'E':
          left()
        case 'C':
          up()
        case 'B':
          down()
  
  for command in commands:
    if p == 2:
      history.clear()

    match command:
      case 'D':
        right()
      case 'E':
        left()
      case 'C':
        up()
      case 'B':
        down()
    
    if cycle:
      break

  if cycle:
    print('ciclo')
  else:
    print(y + 1, x + 1)