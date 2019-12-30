'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
a = [1,2,3,4,5,6,7,8]
b = [3,5,7,8,23,53,72,61,42]

similar = []


for i in a:
    if i in b:
        similar.append(i)
        
unique1 = a.copy()
unique2 = b.copy()
for i in a:
    if i in similar:
        unique1.remove(i)
        
for i in b:
    if i in similar:
        unique2.remove(i)        

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