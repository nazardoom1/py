'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.


0; -1; -2;          tie;  win;  loss; 
1;  0; -1;          loss; tie;  win;
2;  1;  0;          win;  loss; tie;

'''
opt = ['rock','scisors','paper']
import random
bot_digit = random.randint(0,2)

'''reading user`s option'''
user_opt = input("Please put your option: ")
while user_opt.lower() not in opt:
    user_opt = input("Invalid input. Please insert rock, scisors or paper. \n")

''' checking winning conditions '''
if opt.index(user_opt.lower()) - bot_digit == 0:
    print("Bot puts " + opt[bot_digit])
    print("Tie! Put a new value: ")
    while user_opt.lower() not in opt:
        user_opt = input("Invalid input. Please insert rock, scisors or paper. \n")
elif opt.index(user_opt.lower()) - bot_digit == 2 or opt.count(user_opt.lower())-1 - bot_digit == -1:
    print("Bot puts " + opt[bot_digit])
    print("You won!")
elif opt.index(user_opt.lower()) - bot_digit == -2 or opt.count(user_opt.lower())-1 - bot_digit == 1:
    print("Bot puts " + opt[bot_digit])
    print("You`ve lost!")
else: print("Something went wrong")