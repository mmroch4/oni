p = int(input())
n = int(input())

tasks = []

for i in range(n):
  start, end = map(int, input().split(' '))

  tasks.append([start, end])
  
tasks = sorted(tasks, key=lambda x:x[1])

current_end = -1
counter = 0

for i in range(n):
  task = tasks[i]
  
  if current_end <= task[0]:
    current_end = task[1]
    counter += 1


print(counter)