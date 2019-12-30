'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Print a number: ")
inp = input()
fin = []
f = 1
while f <= int(inp):
    if int(inp)%f == 0:
        fin.append(f)
    f += 1
print("Your number divisors: ")
print(fin)