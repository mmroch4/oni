[n,m] = input().split()
n = int(n)
m = int(m)

collected = input().split()

has = set(collected)

print(n - len(has))