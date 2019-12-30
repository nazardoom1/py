
import random
a = [1,2,3,4,5,6,7,8]
b = [3,5,7,8,23,53,72,61,42]


x = 0
for x in range(10):
  a.append(random.randint(1,100)) 
  b.append(random.randint(1,100))
  x +=x


unique1 = []
unique2 = []
similar = []

i = 0
k = 0
if len(a) < len(b):
    min = len(a)
    max = len(b)
else:
    min = len(b)
    max = len(a)

while i < min:
    k = 0
    while k < max:
        if a[i] == b[k]:
            if a[i] in similar:
                break
            else: 
                similar.append(a[i])
        else: k +=1
    i+=1   

unique1 = a.copy()
unique2 = b.copy()
i = 0
while i < len(similar):
    unique1.remove(similar[i])
    i+=1
i = 0
while i < len(similar):    
    unique2.remove(similar[i])
    i+=1

print("Here are the lists: ")
print("List A: ")
print(a)
print("List B: ")
print(b)
print("List A unique elements: ")
print(unique1)
print("List B unique elements: ")
print(unique2)
print("Similar elements from both lists: ")
print(similar)