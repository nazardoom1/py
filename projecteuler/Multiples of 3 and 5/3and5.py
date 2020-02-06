sequence = 1
list = []
while (sequence < 1000):
  if sequence % 3 == 0 or sequence % 5 == 0:
    list.append(sequence)
  sequence = sequence + 1
print(list)
