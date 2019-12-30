'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
digit = random.randint(0,101)

def guess(digit):
    user = input("Put your guess: ")
    while True:
        if int(user) == digit:
            print("Correct!")
            return 0
        elif int(user) < digit:
            user = input("Wrong. Put a bigger one: ")
        elif int(user) > digit:
            user = input("Wrong. Put a smaller one: ")

while True:
    if guess(digit) == 0:
        f = input("Put 'exit' to stop or click enter to continue")
        if f.lower() == "exit":
            break
        else:
            digit = random.randint(0,101)
            guess(digit)
    
        