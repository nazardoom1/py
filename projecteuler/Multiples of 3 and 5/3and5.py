sequence = 1
res = 0
while (sequence < 1000):
  if sequence % 3 == 0 or sequence % 5 == 0:
    res = res + sequence
  sequence = sequence + 1
print(res)
