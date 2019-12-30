'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print("Hi there, input your name here: ")
name = input()
print("Great, now tell me how old you are: ")
age = input()
if int(age) > 100:
    print("You're old, go away")
else:
    hund = 100 - int(age) + 2019
    print("You turn 100 in " + str(hund) + " year!")